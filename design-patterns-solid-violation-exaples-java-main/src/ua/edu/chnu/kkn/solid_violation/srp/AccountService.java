package ua.edu.chnu.kkn.solid_violation.srp;

public class AccountService {

    private TransactionRepository transactionRepository;

    public AccountService(TransactionRepository transactionRepository) {
        this.transactionRepository = transactionRepository;
    }

    public void deposit(int amount) {
        transactionRepository.add(transactionWith(amount));
    }

    public void withdraw(int amount) {
        transactionRepository.add(transactionWith(-amount));
    }

    private Transaction transactionWith(int amount) {
        return new Transaction(new Clock().today(), amount);
    }
}
