const db = require('./../config/mssqlConnection');

exports.savePayCash = async (dataResTrans, expirationDate, user, product, userAddress, transactionValue, amount, res) => {
    const request = new db.Request();
    const query = `INSERT INTO pagos_efectivo (code, orderID, transactionID, state, expirationDate, urlpayment_pdf, urlpayment_html,reference, paymentNetwork, idUsuario, idProducto, cantidad, pol_state, user_address, user_name, value_transaction, title_product, image_product)
    VALUES (
    '${dataResTrans.code}',
    '${dataResTrans.transactionResponse.orderId}',
    '${dataResTrans.transactionResponse.transactionId}',
    '${dataResTrans.transactionResponse.state}',
    '${expirationDate}',
    '${dataResTrans.transactionResponse.extraParameters ? dataResTrans.transactionResponse.extraParameters.URL_PAYMENT_RECEIPT_PDF : ''}',
    '${dataResTrans.transactionResponse.extraParameters ? dataResTrans.transactionResponse.extraParameters.URL_PAYMENT_RECEIPT_HTML: ''}',
    '${dataResTrans.transactionResponse.extraParameters ? dataResTrans.transactionResponse.extraParameters.REFERENCE : ''}',
    '${dataResTrans.transactionResponse.additionalInfo ? dataResTrans.transactionResponse.additionalInfo.paymentNetwork : ''}',
    '${user.user_id}',
    '${product.Resultados.id_Producto}',
    '${amount}',
    '0',
    '${userAddress}',
    '${user.name} ${user.lastname}',
    '${transactionValue}',
    '${product.Resultados.titulo}',
    '${product.Resultados.imagenes_Producto[0]}'
    );`;

    try {
        const recordSet = await request.query(query);
        res(null, recordSet);
    } catch (error) {
        console.log(error);
        res(error, null);
    }
};

exports.savePayCardCredit = async (dataResTrans, user, product, userAddress, transactionValue, amount, res) => {
    const request = new db.Request();
    const query = `INSERT INTO pagos_tarjeta_credito (code, orderID, transactionID, state, paymentNetworkResponseCode, responseCode,responseMessage, paymentNetwork, rejectionType, idUsuario, idProducto, cantidad, transactionDate, transactionTime, pol_state, user_address, user_name, value_transaction, title_product, image_product)
    VALUES (
    '${dataResTrans.code}',
    '${dataResTrans.transactionResponse.orderId ? dataResTrans.transactionResponse.orderId : 0 }',
    '${dataResTrans.transactionResponse.transactionId ? dataResTrans.transactionResponse.transactionId : 0}',
    '${dataResTrans.transactionResponse.state ? dataResTrans.transactionResponse.state : ''}',
    '${dataResTrans.transactionResponse.paymentNetworkResponseCode ? dataResTrans.transactionResponse.paymentNetworkResponseCode : ''}',
    '${dataResTrans.transactionResponse.responseCode ? dataResTrans.transactionResponse.responseCode : ''}',
    '${dataResTrans.transactionResponse.responseMessage ? dataResTrans.transactionResponse.responseMessage : ''}',
    '${dataResTrans.transactionResponse.additionalInfo ? dataResTrans.transactionResponse.additionalInfo.paymentNetwork:''}',
    '${dataResTrans.transactionResponse.additionalInfo ? dataResTrans.transactionResponse.additionalInfo.rejectionType:'' }',
    '${user.user_id}',
    '${product.Resultados.id_Producto}',
    '${amount}',
    '${dataResTrans.transactionResponse.transactionDate ? dataResTrans.transactionResponse.transactionDate : 0 }',
    '${dataResTrans.transactionResponse.transactionTime ? dataResTrans.transactionResponse.transactionTime : 0}',
    '0',
    '${userAddress}',
    '${user.name} ${user.lastname}',
    '${transactionValue}',
    '${product.Resultados.titulo}',
    '${product.Resultados.imagenes_Producto[0]}'
    );`;
    
    try {
        const recordSet = await request.query(query);
        res(null, recordSet);
    } catch (error) {
        console.log(error);
        res(error, null);
    }
};

exports.savePayPSE = async (dataResTrans, user, product, userAddress, transactionValue, amount, res) => {
    const request = new db.Request();
    const query = `INSERT INTO pagos_pse (code, orderID, transactionID, state, paymentNetworkResponseCode, responseCode,responseMessage,  idUsuario, idProducto, cantidad, transactionDate, transactionTime, pol_state, user_address, user_name, value_transaction, title_product, image_product)
    VALUES (
    '${dataResTrans.code}',
    '${dataResTrans.transactionResponse.orderId}',
    '${dataResTrans.transactionResponse.transactionId}',
    '${dataResTrans.transactionResponse.state}',
    '${dataResTrans.transactionResponse.paymentNetworkResponseCode}',
    '${dataResTrans.transactionResponse.responseCode}',
    '${dataResTrans.transactionResponse.responseMessage}',
    '${user.user_id}',
    '${product.Resultados.id_Producto}',
    '${amount}',
    '${new Date().toISOString().slice(0, 10)}',
    '${new Date().getHours()}:${new Date().getMinutes()}:${new Date().getSeconds()}',
    '0',
    '${userAddress}',
    '${user.name} ${user.lastname}',
    '${transactionValue}',
    '${product.Resultados.titulo}',
    '${product.Resultados.imagenes_Producto[0]}'
    );`;

    try {
        const recordSet = await request.query(query);
        res(null, recordSet);
    } catch (error) {
        console.log(error);
        res(error, null);
    }
};

exports.getContactForm = async () => {
    const request = new db.Request();
    const query = `SELECT * FROM contact_form_kiero`;
    try {
        const recordSet = await request.query(query);
        return recordSet.recordset[0];
    } catch (error) {
        console.log(error);
    }
};

/* 
    3778 1474 0125 637
    79479166
    gustavo a baez c
    0704
    11/2020
*/