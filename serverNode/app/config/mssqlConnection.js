const sql = require('mssql');

const config = {
    server: '190.85.232.78',
    user: 'sa',
    password: 'S3rv3r1-27!',
    database: 'DBKiero_Productos'
};

sql.connect(config, function (err) {
    if (err) {
        console.error('Error connecting: ' + err.stack);
        return;
    }
    console.log('Connection established');
});

module.exports = sql;
