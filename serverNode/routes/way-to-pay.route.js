const express = require('express');
const router = express.Router();
const wayToPayController = require(__dirname + "/../app/controllers/way-to-pay.controller.js");

router.get('/', wayToPayController.getBanksPSE);
router.post('/cash', wayToPayController.payCash);
router.post('/credit', wayToPayController.payCardCredit);
router.post('/pse', wayToPayController.payTransactionPSE);

module.exports = router;