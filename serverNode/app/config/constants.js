// prod
const apiKey = 'uzIc90bkpXj0aJDh22H67MRJnl';

// test
/* const apiKey = '4Vj8eK4rloUd272L48hsrarnUA'; */

// prod
const apiLogin = 'UGgWoot5rOHJvxv';

// test
/* const apiLogin = 'pRRXKOl8ikMmt9u'; */

// prod
const accountId = '532826';

// test
/* const accountId = '512321'; */

const notifyUrlCredit = 'https://kieroapi.net/listen-to-payu/credit';
const notifyUrlCash = 'https://kieroapi.net/listen-to-payu/cash';
const notifyUrlPSE = 'https://kieroapi.net/listen-to-payu/pse';

exports.jsonCash = {
   "language": "es",
   "command": "SUBMIT_TRANSACTION",
   "merchant": {
      "apiKey": apiKey,
      "apiLogin": apiLogin
   },
   "transaction": {
      "order": {
         "accountId": accountId,
         "referenceCode": "TestPayU",
         "description": "payment test",
         "language": "es",
         "signature": "7ee7cf808ce6a39b17481c54f2c57acc",
         "notifyUrl": notifyUrlCash,
         "additionalValues": {
            "TX_VALUE": {
               "value": 20000,
               "currency": "COP"
            },
            "TX_TAX": {
               "value": 3193,
               "currency": "COP"
            },
            "TX_TAX_RETURN_BASE": {
               "value": 16806,
               "currency": "COP"
            }
         },
         "buyer": {
            "fullName": "First name and last name",
            "emailAddress": "buyer_test@test.com"
         }
      },
      "type": "AUTHORIZATION_AND_CAPTURE",
      "paymentMethod": 'BALOTO',
      "expirationDate": "2017-05-10T00:00:00",
      "paymentCountry": "CO",
      "ipAddress": "127.0.0.1"
   },
   "test": false
};

exports.jsonCardCredit = {
   "language": "es",
   "command": "SUBMIT_TRANSACTION",
   "merchant": {
      "apiKey": apiKey,
      "apiLogin": apiLogin
   },
   "transaction": {
      "order": {
         "accountId": accountId,
         "referenceCode": "TestPayU",
         "description": "payment test",
         "language": "es",
         "signature": "7ee7cf808ce6a39b17481c54f2c57acc",
         "notifyUrl": notifyUrlCredit,
         "additionalValues": {
            "TX_VALUE": {
               "value": 20000,
               "currency": "COP"
            },
            "TX_TAX": {
               "value": 3193,
               "currency": "COP"
            },
            "TX_TAX_RETURN_BASE": {
               "value": 16806,
               "currency": "COP"
            }
         },
         "buyer": {
            "merchantBuyerId": "1",
            "fullName": "First name and second buyer  name",
            "emailAddress": "buyer_test@test.com",
            "contactPhone": "7563126",
            "dniNumber": "5415668464654",
            "shippingAddress": {
               "street1": "calle 100",
               "street2": "5555487",
               "city": "Medellin",
               "state": "Antioquia",
               "country": "CO",
               "postalCode": "000000",
               "phone": "7563126"
            }
         },
         "shippingAddress": {
            "street1": "calle 100",
            "street2": "5555487",
            "city": "Medellin",
            "state": "Antioquia",
            "country": "CO",
            "postalCode": "0000000",
            "phone": "7563126"
         }
      },
      "payer": {
         "merchantPayerId": "1",
         "fullName": "First name and second payer name",
         "emailAddress": "payer_test@test.com",
         "contactPhone": "7563126",
         "dniNumber": "5415668464654",
         "billingAddress": {
            "street1": "calle 93",
            "street2": "125544",
            "city": "Bogota",
            "state": "Bogota DC",
            "country": "CO",
            "postalCode": "000000",
            "phone": "7563126"
         }
      },
      "creditCard": {
         "number": "4097440000000004",
         "securityCode": "321",
         "expirationDate": "2014/12",
         "name": "REJECTED"
      },
      "extraParameters": {
         "INSTALLMENTS_NUMBER": 1
      },
      "type": "AUTHORIZATION_AND_CAPTURE",
      "paymentMethod": "VISA",
      "paymentCountry": "CO",
      "deviceSessionId": "vghs6tvkcle931686k1900o6e1",
      "ipAddress": "127.0.0.1",
      "cookie": "pt1t38347bs6jc9ruv2ecpv7o2",
      "userAgent": "Mozilla/5.0 (Windows NT 5.1; rv:18.0) Gecko/20100101 Firefox/18.0"
   },
   "test": false
};

exports.jsonPSE = {
   "language": "es",
   "command": "GET_BANKS_LIST",
   "merchant": {
      "apiLogin": apiLogin,
      "apiKey": apiKey
   },
   "test": false,
   "bankListInformation": {
      "paymentMethod": "PSE",
      "paymentCountry": "CO"
   }
};

exports.jsonPayPSE = {
   "language": "es",
   "command": "SUBMIT_TRANSACTION",
   "merchant": {
      "apiKey": apiKey,
      "apiLogin": apiLogin
   },
   "transaction": {
      "order": {
         "accountId": accountId,
         "referenceCode": "TestPayU",
         "description": "payment test",
         "language": "es",
         "signature": "7ee7cf808ce6a39b17481c54f2c57acc",
         "notifyUrl": notifyUrlPSE,
         "additionalValues": {
            "TX_VALUE": {
               "value": 20000,
               "currency": "COP"
            },
            "TX_TAX": {
               "value": 3193,
               "currency": "COP"
            },
            "TX_TAX_RETURN_BASE": {
               "value": 16806,
               "currency": "COP"
            }
         },
         "buyer": {
            "emailAddress": "buyer_test@test.com"
         }
      },
      "payer": {
         "fullName": "First name and second payer name",
         "emailAddress": "payer_test@test.com",
         "contactPhone": "7563126"
      },
      "extraParameters": {
         "RESPONSE_URL": "http://www.test.com/response",
         "PSE_REFERENCE1": "127.0.0.1",
         "FINANCIAL_INSTITUTION_CODE": "1007",
         "USER_TYPE": "N",
         "PSE_REFERENCE2": "CC",
         "PSE_REFERENCE3": "123456789"
      },
      "type": "AUTHORIZATION_AND_CAPTURE",
      "paymentMethod": "PSE",
      "paymentCountry": "CO",
      "ipAddress": "127.0.0.1",
      "cookie": "pt1t38347bs6jc9ruv2ecpv7o2",
      "userAgent": "Mozilla/5.0 (Windows NT 5.1; rv:18.0) Gecko/20100101 Firefox/18.0"
   },
   "test": false
};

// prod
exports.merchantId = '530932';

// test
/* exports.merchantId = '508029'; */