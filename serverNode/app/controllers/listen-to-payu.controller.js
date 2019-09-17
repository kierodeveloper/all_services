const listenToPayuModel = require(__dirname + '/../models/listen-to-payu.model');
const main = require('./../../lib/functions/main');

const addressNoticationTrans = ['yuli.espitia2@kiero.co', 'gloria.castaneda@kiero.co',
                                'gustavo.baez@kiero.co', 'jose.mz@kiero.co', 'jose.marin@kiero.co'];
                                
/* const addressNoticationTrans = ['damaos530@gmail.com']; */

exports.listenToCredit = (async (req, res) => {
    //console.log('listenToCredit', req.body);
    const polState = req.body.state_pol;
    const transactionId = req.body.transaction_id;
    listenToPayuModel.updateStateTransCreditCard(transactionId, polState, (err, updateTrans) => {
        if (err) throw err;

        if (polState == 4) { 
            listenToPayuModel.getDataUserTransactionCredit(transactionId, (err, dataUserTrans) => {
                if (err) console.error(err);
                main.sendEmail(addressNoticationTrans, main.generateEmailTemplate(dataUserTrans));
            });
        }

        res.send({ status: true });
        return console.log(`Tran credit update with id ${transactionId} and state ${polState}`);
    });
});

exports.listenToCash = (async (req, res) => {
    //console.log('entro al cash')
    //console.log('listenToCash', req.body);
	//return res.send({status:req.body})
    const polState = req.body.state_pol;
console.log("variable 1",polState)
    const transactionId = req.body.transaction_id;
    listenToPayuModel.updateStateTransCash(transactionId, polState, (err, updateTrans) => {

        if (err) throw err;
       //console.log('asdgaksudygkauygdqwkyugdakygdjakwgdkawudikauwgdiakuwgdkaugwdkiawugdaikuwgdaiwugdkaiwugaikwugdaiuwgdkaiwugdkaiwaiwudgaiwudgakiugakiudgkaiw')
        if (polState == 4) { 
            listenToPayuModel.getDataUserTransactionCash(transactionId, (err, dataUserTrans) => {
                if (err) console.error(err);
                main.sendEmail(addressNoticationTrans, main.generateEmailTemplate(dataUserTrans));
            });
        }

        res.send({ status: true });
        return console.log(`Tran cash update with id ${transactionId} and state ${polState}`);
    });
});

exports.listenToPSE = (async (req, res) => {
    console.log('listenToPSE', req.body);
    const polState = req.body.state_pol;
    const transactionId = req.body.transaction_id;
    listenToPayuModel.updateStateTransPSE(transactionId, polState, (err, updateTrans) => {
        if (err) throw err;
        
        if (polState == 4) { 
            listenToPayuModel.getDataUserTransactionPSE(transactionId, (err, dataUserTrans) => {
                if (err) console.error(err);
                main.sendEmail(addressNoticationTrans, main.generateEmailTemplate(dataUserTrans));
            });
        }

        res.send({ status: true });
        return console.log(`Tran pse update with id ${transactionId} and state ${polState}`);
    });
});
