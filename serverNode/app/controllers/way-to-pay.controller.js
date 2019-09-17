const constants = require('./../config/constants');
const wayToPayModel = require(__dirname + '/../models/way-to-pay.model.js');
const axios = require('axios');
// class
const main = require('../../lib/functions/main');

// payU test
/* const apiPayU = 'https://sandbox.api.payulatam.com/payments-api/4.0/service.cgi'; */

// payU prod
const apiPayU = 'https://api.payulatam.com/payments-api/4.0/service.cgi';

exports.getBanksPSE = (async (req, res) => {
  const jsonPSE = constants.jsonPSE;
  try {
    const resPayU = await axios.post(apiPayU, jsonPSE);
    resPayU.data.banks.map((elem) => {
      elem.active = false;

    });
    resPayU.data.banks = resPayU.data.banks.filter(elem => elem.pseCode != '0');
    res.send(resPayU.data);
  } catch (error) {
    console.error(error);
  }
});

exports.payCardCredit = (async (req, res) => {
  const jsonCardCredit = constants.jsonCardCredit;
  const card = req.body.card;
  const product = req.body.product.Resultados;
  const user = req.body.user;
  const address = req.body.user.addresses.filter(elem => elem.selected)[0];
  const amount = req.body.amount;
  const ipUser = req.body.ip;

  /*  construct the json for then send */
  // product
  jsonCardCredit.transaction.order.description = product.titulo;
  jsonCardCredit.transaction.order.additionalValues.TX_VALUE.value = (product.precio * amount);
  jsonCardCredit.transaction.order.additionalValues.TX_TAX.value = (jsonCardCredit.transaction.order.additionalValues.TX_VALUE.value * 19) / 100;
  jsonCardCredit.transaction.order.additionalValues.TX_TAX_RETURN_BASE.value = parseFloat(
    jsonCardCredit.transaction.order.additionalValues.TX_VALUE.value - jsonCardCredit.transaction.order.additionalValues.TX_TAX.value // calculate the total price (iva-subtotal)
  );

  // reference and signature
  jsonCardCredit.transaction.order.referenceCode = main.referenceCode(product.id_Producto); // generate the reference code of the transaction
  jsonCardCredit.transaction.order.signature = main.generateRandomSignature( // generate the signature for the request
    jsonCardCredit.merchant.apiKey,
    constants.merchantId,
    jsonCardCredit.transaction.order.referenceCode,
    jsonCardCredit.transaction.order.additionalValues.TX_VALUE.value,
    jsonCardCredit.transaction.order.additionalValues.TX_TAX_RETURN_BASE.currency
  );

  // buyer data
  jsonCardCredit.transaction.order.buyer.merchantBuyerId = user.user_id;
  jsonCardCredit.transaction.order.buyer.fullName = card.name;
  jsonCardCredit.transaction.order.buyer.contactPhone = user.number_phone ? user.number_phone : ''; // this number must change for real
  jsonCardCredit.transaction.order.buyer.emailAddress = user.email;
  jsonCardCredit.transaction.order.buyer.dniNumber = card.numberDoc;
  jsonCardCredit.transaction.order.buyer.shippingAddress.street1 = `${address.via} ${address.number_via}`;
  jsonCardCredit.transaction.order.buyer.shippingAddress.street2 = `${address.via} ${address.number_via}`;
  jsonCardCredit.transaction.order.buyer.shippingAddress.city = address.city ? address.city : '';
  jsonCardCredit.transaction.order.buyer.shippingAddress.state = address.department ? address.department : '';
  jsonCardCredit.transaction.order.buyer.shippingAddress.country = 'CO'; // this bit will be change for real user country
  jsonCardCredit.transaction.order.buyer.shippingAddress.postalCode = '57'; // this bit will be change for real user postal country
  jsonCardCredit.transaction.order.buyer.shippingAddress.phone = address.number_contact ? address.number_contact : '';

  // shippingAddress
  // !!! this data must change for real data !!!!
  jsonCardCredit.transaction.order.shippingAddress.street1 = `${address.via} ${address.number_via}`;
  jsonCardCredit.transaction.order.shippingAddress.street2 = `${address.via} ${address.number_via}`;
  jsonCardCredit.transaction.order.shippingAddress.city = address.city ? address.city : '';
  jsonCardCredit.transaction.order.shippingAddress.state = address.department ? address.department : '';
  jsonCardCredit.transaction.order.shippingAddress.country = 'CO';
  jsonCardCredit.transaction.order.shippingAddress.postalCode = '57';
  jsonCardCredit.transaction.order.shippingAddress.phone = address.number_contact;

  // credit card
  jsonCardCredit.transaction.creditCard.number = card.numberCredit.replace(/\s/g, '');
  jsonCardCredit.transaction.creditCard.securityCode = card.cvv;
  jsonCardCredit.transaction.creditCard.expirationDate = `${card.year}/${card.month}`;
  jsonCardCredit.transaction.creditCard.name = card.name;

  // Otional data
  jsonCardCredit.transaction.paymentMethod = card.paymentMethod;
  jsonCardCredit.transaction.paymentCountry = 'CO';
  jsonCardCredit.transaction.deviceSessionId = Math.floor(1000000 + Math.random() * 1900000);
  jsonCardCredit.transaction.ipAddress = ipUser;
  jsonCardCredit.transaction.cookie = Math.floor(1000000 + Math.random() * 1900000);
  jsonCardCredit.transaction.userAgent = req.headers['user-agent'];

  // payer data
  jsonCardCredit.transaction.payer.merchantPayerId = user.user_id;
  jsonCardCredit.transaction.payer.fullName = card.name;
  jsonCardCredit.transaction.payer.emailAddress = user.email;
  jsonCardCredit.transaction.payer.contactPhone = user.number_phone ? user.number_phone : ''; // this number must change for real
  jsonCardCredit.transaction.payer.dniNumber = card.numberDoc;
  jsonCardCredit.transaction.payer.billingAddress.street1 = `${address.via} ${address.number_via}`;
  jsonCardCredit.transaction.payer.billingAddress.street2 =`${address.via} ${address.number_via}`;
  jsonCardCredit.transaction.payer.billingAddress.city = address.city ? address.city : '';
  jsonCardCredit.transaction.payer.billingAddress.state = address.department ? address.department : '';
  jsonCardCredit.transaction.payer.billingAddress.country = 'CO'; // this bit will be change for real user country
  jsonCardCredit.transaction.payer.billingAddress.postalCode =  '57';
  jsonCardCredit.transaction.payer.billingAddress.phone = address.number_contact;
  jsonCardCredit.transaction.payer.dniType = card.typeDoc;

  try {
    const resPayU = await axios.post(apiPayU, jsonCardCredit);
    wayToPayModel.savePayCardCredit(resPayU.data, user, req.body.product, `${address.via}%${address.number_via}%${address.city}%${address.department}%${address.number_contact}`, jsonCardCredit.transaction.order.additionalValues.TX_VALUE.value, amount, (err, saveData) => {
      if (err) {
        return res.send({
          status: false,
          data: null,
          err: err
        });
      } else {
        return res.send({
          status: true,
          data: resPayU.data.transactionResponse,
          err: null
        });
      }
    });
  } catch (error) {
    console.error(error);
    return res.send({
      status: false,
      data: null,
      err: error
    });
  }
});

exports.payCash = (async (req, res) => {
 console.log("Holaaaaaaaaa") 
const today = new Date();
  const expirationDate = new Date();
  expirationDate.setDate(today.getDate() + 4);

  const paymentMethod = req.body.type;
  const product = req.body.product.Resultados;
  const user = req.body.user;
  const amount = req.body.amount;
  const address = req.body.user.addresses.filter(elem => elem.selected)[0];
  const ipUser = req.body.ip;
  const jsonCash = constants.jsonCash;

  /*  construct the json for then send */
  jsonCash.transaction.order.description = product.titulo;
  jsonCash.transaction.paymentMethod = paymentMethod;
  jsonCash.transaction.order.additionalValues.TX_VALUE.value = (product.precio * amount);
  jsonCash.transaction.order.additionalValues.TX_TAX.value = (jsonCash.transaction.order.additionalValues.TX_VALUE.value * 19) / 100;
  jsonCash.transaction.expirationDate = expirationDate;
  jsonCash.transaction.ipAddress = ipUser;

  // buyer
  jsonCash.transaction.order.buyer.fullName = `${user.name} ${user.lastname}`;
  jsonCash.transaction.order.buyer.emailAddress = user.email;

  jsonCash.transaction.order.additionalValues.TX_TAX_RETURN_BASE.value = parseFloat(
    jsonCash.transaction.order.additionalValues.TX_VALUE.value - jsonCash.transaction.order.additionalValues.TX_TAX.value // calculate the total price (iva-subtotal)
  );
  jsonCash.transaction.order.referenceCode = main.referenceCode(product.id_Producto); // generate the reference code of the transaction
  jsonCash.transaction.order.signature = main.generateRandomSignature( // generate the signature for the request
    jsonCash.merchant.apiKey,
    constants.merchantId,
    jsonCash.transaction.order.referenceCode,
    jsonCash.transaction.order.additionalValues.TX_VALUE.value,
    jsonCash.transaction.order.additionalValues.TX_TAX_RETURN_BASE.currency
  );
  try {
    const resPayU = await axios.post(apiPayU, jsonCash);
    const expirationDateInt = `${expirationDate.getFullYear()}0${expirationDate.getMonth() + 1}${expirationDate.getDate()}`;
    wayToPayModel.savePayCash(resPayU.data, parseInt(expirationDateInt), user, req.body.product, `${address.via}%${address.number_via}%${address.city}%${address.department}%${address.number_contact}`,  jsonCash.transaction.order.additionalValues.TX_VALUE.value, amount, (err, saveData) => {
      if (err) {
        return res.send({
          status: false,
          data: null,
          err: err
        });
      } else {
        return res.send({
          status: true,
          data: resPayU.data.transactionResponse,
          err: null
        });
      }
    });
  } catch (error) {
    console.error(error);
    return res.send({
      status: false,
      data: null,
      err: error
    });
  }
});

exports.payTransactionPSE = (async (req, res) => {
  const jsonPayPSE = constants.jsonPayPSE;
  const product = req.body.product.Resultados;
  const user = req.body.user;
  const address = req.body.user.addresses.filter(elem => elem.selected)[0];
  const amount = req.body.amount;
  const ipUser = req.body.ip;
  const bank = req.body.bank;

  /*  construct the json for then send */
  // product
  jsonPayPSE.transaction.order.description = product.titulo;
  jsonPayPSE.transaction.order.additionalValues.TX_VALUE.value = (product.precio * amount);
  jsonPayPSE.transaction.order.additionalValues.TX_TAX.value = (jsonPayPSE.transaction.order.additionalValues.TX_VALUE.value * 19) / 100;
  jsonPayPSE.transaction.order.additionalValues.TX_TAX_RETURN_BASE.value = parseFloat(
    jsonPayPSE.transaction.order.additionalValues.TX_VALUE.value - jsonPayPSE.transaction.order.additionalValues.TX_TAX.value // calculate the total price (iva-subtotal)
  );

  // reference and signature
  jsonPayPSE.transaction.order.referenceCode = main.referenceCode(product.id_Producto); // generate the reference code of the transaction
  jsonPayPSE.transaction.order.signature = main.generateRandomSignature( // generate the signature for the request
    jsonPayPSE.merchant.apiKey,
    constants.merchantId,
    jsonPayPSE.transaction.order.referenceCode,
    jsonPayPSE.transaction.order.additionalValues.TX_VALUE.value,
    jsonPayPSE.transaction.order.additionalValues.TX_TAX_RETURN_BASE.currency
  );

  // buyer data
  jsonPayPSE.transaction.order.buyer.emailAddress = user.email;

  // Otional data
  jsonPayPSE.transaction.paymentCountry = 'CO';
  jsonPayPSE.transaction.ipAddress = ipUser;
  jsonPayPSE.transaction.cookie = Math.floor(1000000 + Math.random() * 1900000);
  jsonPayPSE.transaction.userAgent = req.headers['user-agent'];

  // payer data
  jsonPayPSE.transaction.payer.fullName = `${user.name} ${user.lastname}`;
  jsonPayPSE.transaction.payer.emailAddress = user.email;
  jsonPayPSE.transaction.payer.contactPhone = user.number_phone ? user.number_phone : '';

  // extraparameters
  jsonPayPSE.transaction.extraParameters.RESPONSE_URL = 'https://www.kiero.co/orders.html'; // url return user
  jsonPayPSE.transaction.extraParameters.PSE_REFERENCE1 = main.getClientIp(req).replace('::ffff:', '');
  jsonPayPSE.transaction.extraParameters.PSE_REFERENCE2 = 'CC'; // here is the user document type
  jsonPayPSE.transaction.extraParameters.USER_TYPE = 'N'; // user type (natural (N) and juridic (J))
  jsonPayPSE.transaction.extraParameters.PSE_REFERENCE3 = user.document_id ? user.document_id : ''; // user document number
  jsonPayPSE.transaction.extraParameters.FINANCIAL_INSTITUTION_CODE = bank.pseCode;

  try {
    const resPayU = await axios.post(apiPayU, jsonPayPSE);
    wayToPayModel.savePayPSE(resPayU.data, user, req.body.product, `${address.via}%${address.number_via}%${address.city}%${address.department}%${address.number_contact}`,  jsonPayPSE.transaction.order.additionalValues.TX_VALUE.value, amount, (err, saveData) => {
      if (err) {
        return res.send({
          status: false,
          data: null,
          err: err
        });
      } else {
        return res.send({
          status: true,
          data: resPayU.data.transactionResponse,
          err: null
        });
      }
    });
  } catch (error) {
    console.error(error);
    return res.send({
      status: false,
      data: null,
      err: error
    });
  }
});
