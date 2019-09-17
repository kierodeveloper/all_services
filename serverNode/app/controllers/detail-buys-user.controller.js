const detailBuysUserModel = require(__dirname + '/../models/detail-buys-user.model');

exports.getDetail = (async (req, res) => {
    const user = req.body.user;
    if (user) {
        detailBuysUserModel.getDetail(user, (err, detailUser) => {
            if (err) {
                res.send({ status: false, data: null, err: err});
            }else {
                res.send({ status: true, data: detailUser, err: null });
            }
        });
    }else {
        res.send({ status: false, data: null, err: 'no provider for user'});
    }
});