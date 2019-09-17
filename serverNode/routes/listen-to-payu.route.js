const express = require('express');
const router = express.Router();
const listenToPayUController = require(__dirname + "/../app/controllers/listen-to-payu.controller");

router.post('/credit', listenToPayUController.listenToCredit);
router.post('/cash', listenToPayUController.listenToCash);
router.post('/pse', listenToPayUController.listenToPSE);

module.exports = router;