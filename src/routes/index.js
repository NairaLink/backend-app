import { Router } from 'express';
import createAccount from '../controllers/createAccount';
import retrieveAccount from '../controllers/retrieveAccount';
import getAccountTransactions from '../controllers/getAccountTransactions';

const router = Router();

router.post('/accounts', createAccount);
router.get('/accounts/:userId', retrieveAccount);
router.get('/accounts/:userId/transactions', getAccountTransactions);
// router.post('/transactions', TransactionController.postTransaction);
// router.get('/transactions', TransactionController.getTransactions);

// router.post('/customers', TransactionController.postCustomer);
// router.get('/customers', TransactionController.getCustomers);

export default router;
