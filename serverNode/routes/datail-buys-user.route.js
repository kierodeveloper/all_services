const express = require('express');
const router = express.Router();
const detailBuysUserController = require(__dirname + "/../app/controllers/detail-buys-user.controller");

router.post('/', detailBuysUserController.getDetail);

module.exports = router;