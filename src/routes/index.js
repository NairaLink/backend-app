import { Router } from 'express';
import createAccount from '../controllers/createAccount';

const router = Router();

router.post('/accounts', createAccount);
// router.post('/transactions', TransactionController.postTransaction);
// router.get('/transactions', TransactionController.getTransactions);

// router.post('/customers', TransactionController.postCustomer);
// router.get('/customers', TransactionController.getCustomers);

export default router;
