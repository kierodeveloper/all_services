const crypto = require('crypto');
const nodemailer = require('nodemailer');

exports.referenceCode = ((idProduct) => {
  const numberCodeRandom = Math.floor(100000 + Math.random() * 900000);
  const date = new Date().toISOString().slice(0, 10).replace('-', '');
  /*  const resRefCode = `KIERO${idProduct}${date}${numberCodeRandom}`; */
  const resRefCode = `KIERO${idProduct}${date}${numberCodeRandom}`;
  return resRefCode;
});

exports.generateRandomSignature = ((apiKey, merchandtId, referenceCode, txValue, currency) => {
  const str = `${apiKey}~${merchandtId}~${referenceCode}~${txValue}~${currency}`;
  const hash = crypto.createHash('sha256').update(str).digest('hex');
  return hash;
});

exports.getClientIp = ((req) => {
  let ipAddress;
  // The request may be forwarded from local web server.
  const forwardedIpsStr = req.header('x-forwarded-for');
  if (forwardedIpsStr) {
    // 'x-forwarded-for' header may return multiple IP addresses in
    // the format: "client IP, proxy 1 IP, proxy 2 IP" so take the
    // the first one
    const forwardedIps = forwardedIpsStr.split(',');
    ipAddress = forwardedIps[0];
  }
  if (!ipAddress) {
    // If request was not forwarded
    ipAddress = req.connection.remoteAddress;
  }
  return ipAddress;
});

exports.sendEmail = ( async (emails, data) => {
  const transporter = nodemailer.createTransport({
    service:'gmail',
    auth: {
        user: 'yuli.espitia2@kiero.co',
        pass: 'Clavesegura2017'
    }
  });

  const mailOptions = {
    from: 'yuli.espitia2@kiero.co',
    to: JSON.stringify(emails),
    subject: 'Kiero | Vendiste un producto!',
    html: data
  };
  const result = await transporter.sendMail(mailOptions);
  return result;
});

exports.generateEmailTemplate = ((data) => {
  const address = data.user_address.split('%');
  const template = 
    `
    <br>
    <br>
    <div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif">
    <div>
        <table>
            <tr>
                <td>
                    <img style="width: 88px; height: 64px" src="https://resourcekiero.s3-us-west-2.amazonaws.com/logo-kiero.png" alt="">
                </td>
                <td>
                    <h1 style="color: #cf0a2c;">Vendiste un producto!</h1>
                </td>
            </tr>
        </table>
        <hr>
    </div>
    <div>
        <h3>Detalle de la compra</h3>
        <table>
            <tr>
                <td>
                  <img style="width: 88px; height: 64px" src=${data.image_product} alt="">
                </td>
                <td>
                    <div>
                        <p>
                        <a href="https://articulo.kiero.co/product-details/?id-${data.idProducto}-${data.title_product}"> 
                        ${data.title_product}</a>
                        </p>
                        <p>
                            Cantidad: ${data.cantidad}
                        </p>
                        <p style="color: #cf0a2c">
                            $${data.value_transaction} c/u 
                        </p>
                    </div>
                </td>
            </tr>
        </table>
        <br>
        <h3>Pago</h3>
        <div>
            <div>
                <p>Producto:  <span style="margin-left: 10px;">$ ${data.value_transaction}</span></p>
            </div>
            <hr align="left" width="9%">
            <div>
                <p>Total: 	<span style="color: #cf0a2c; margin-left: 36px;">$ ${data.value_transaction}</span></p>
            </div>
        </div>
        <br>
        <div>
            <h3>Envio</h3>
            <div>
                <p>${address[0]} #${address[1]} </p>
                <p>${address[2]}, ${address[3]}</p>
                <p>${data.user_name}</p>   
                <p>${address[4]}</p>     
            </div>
        </div>
        <br>
        <div>
            <h3>Comprador</h3>
            <div>
                <p>${data.user_name}</p>
                <a href="https://www.kiero.co/">Enviar mensaje</a>
            </div>
            <br>
            <p>${address[2]}, ${address[3]}</p>
        </div>
        <br>
        <div>
            <h5>Equipo Kiero International Group</h5>
        </div>
    </div>
    <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,400&display=swap" rel="stylesheet">
    </div>`;

    return template;
});