const Account = require('../models/Account')
const Transaction = require('../models/Transaction')
const { Op } = require('sequelize')

module.exports = async (req, res, next) => {
  try {
    const { userId } = req.params

    const account = await Account.findOne({ userId })

    if (!account) {
      return res.status(404).json({ message: 'Account not found' })
    }

    const transactions = await Transaction.findAll({
      where: {
        [Op.or]: [
          { fromAccount: account.accountNumber },
          { toAccount: account.accountNumber },
        ],
      },
    })

    return res.status(200).json(transactions)
  } catch (error) {
    console.log(error)
    next(error)
  }
}
