const db = require('./../config/mssqlConnection');

exports.getDetail = async (user, res) => {
    const request = new db.Request();

    // GET BUYS PSE
    const queryPSE = `SELECT * FROM pagos_pse WHERE idUsuario = '${user}';`;
    const recordPSE = await request.query(queryPSE);

    // GET BUYS PSE
    const queryCash = `SELECT * FROM pagos_efectivo WHERE idUsuario = '${user}';`;
    const recordCash = await request.query(queryCash);

    // GET BUYS CREDIT CARD
    const queryCard = `SELECT * FROM pagos_tarjeta_credito WHERE idUsuario = '${user}';`;
    const recordCard = await request.query(queryCard);

    const data = { 
        pse: recordPSE.recordset,
        cash: recordCash.recordset,
        card: recordCard.recordset
    };

    res(null, data);
};
