const db = require('./../config/mssqlConnection');

exports.updateStateTransPSE = async (transactionId, polState, res) => {
    const request = new db.Request();
    const query = `UPDATE pagos_pse SET pol_state = '${polState}' WHERE transactionID = '${transactionId}'`;
    try {
        const recordSet = await request.query(query);
        res(null, recordSet);
    } catch (error) {
        console.log(error);
        res(error, null);
    }
};

exports.updateStateTransCreditCard = async (transactionId, polState, res) => {
    const request = new db.Request();
    const query = `UPDATE pagos_tarjeta_credito SET pol_state = '${polState}' WHERE transactionID = '${transactionId}'`;
    try {
        const recordSet = await request.query(query);
        res(null, recordSet);
    } catch (error) {
        console.log(error);
        res(error, null);
    }
};

exports.updateStateTransCash = async (transactionId, polState, res) => {
    const request = new db.Request();
    const query = `UPDATE pagos_efectivo SET pol_state = '${polState}' WHERE transactionID = '${transactionId}'`;
console.log(query)
    try {
        const recordSet = await request.query(query);
        res(null, recordSet);
    } catch (error) {
        console.log(error);
        res(error, null);
    }
};


exports.getDataUserTransactionCash = (async (transactionID, res) => {
    const request = new db.Request();
    const query = `SELECT  * FROM pagos_efectivo WHERE transactionID = '${transactionID}' ;`;
    try {
        const recordSet = await request.query(query);
        res(null, recordSet.recordset[0]);
    } catch (error) {
        res(error, null);
    }
});

exports.getDataUserTransactionCredit = (async (transactionID, res) => {
    const request = new db.Request();
    const query = `SELECT  * FROM pagos_tarjeta_credito  WHERE transactionID = '${transactionID}' ;`;
    try {
        const recordSet = await request.query(query);
        res(null, recordSet.recordset[0]);
    } catch (error) {
        res(error, null);
    }
});

exports.getDataUserTransactionPSE = (async (transactionID, res) => {
    const request = new db.Request();
    const query = `SELECT  * FROM pagos_pse  WHERE transactionID = '${transactionID}' ;`;
    try {
        const recordSet = await request.query(query);
        res(null, recordSet.recordset[0]);
    } catch (error) {
        res(error, null);
    }
});
