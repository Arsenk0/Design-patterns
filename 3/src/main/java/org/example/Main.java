package org.example;

import org.example.di.DaggerAppComponent;
import org.example.model.Expense;
import org.example.service.ExpenseService;
import org.example.util.InputUtil;

import javax.inject.Inject;
import java.util.List;

public class Main {

    @Inject
    ExpenseService expenseService;

    public static void main(String[] args) {
        Main main = new Main();
        DaggerAppComponent.create().inject(main);
        main.run();
    }

    public void run() {
        while (true) {
            System.out.println("Меню:");
            System.out.println("1. Додати витрату");
            System.out.println("2. Показати всі витрати");
            System.out.println("3. Оновити витрату");
            System.out.println("4. Видалити витрату");
            System.out.println("5. Сортувати витрати за сумою");
            System.out.println("6. Сортувати витрати за датою");
            System.out.println("7. Пошук витрат");
            System.out.println("8. Вийти");
            System.out.print("Вибір: ");
            int choice = InputUtil.readInt();

            switch (choice) {
                case 1:
                    System.out.print("Введіть назву витрати: ");
                    String name = InputUtil.readLine();
                    System.out.print("Введіть суму витрати: ");
                    double amount = InputUtil.readDouble();
                    System.out.print("Введіть дату витрати (YYYY-MM-DD): ");
                    String date = InputUtil.readLine();
                    expenseService.addExpense(new Expense(name, amount, date));
                    break;
                case 2:
                    expenseService.getAllExpenses().forEach(System.out::println);
                    break;
                case 3:
                    System.out.print("Введіть назву витрати: ");
                    String updName = InputUtil.readLine();
                    System.out.print("Введіть нову суму: ");
                    double updAmt = InputUtil.readDouble();
                    System.out.print("Введіть нову дату: ");
                    String updDate = InputUtil.readLine();
                    expenseService.updateExpense(updName, updAmt, updDate);
                    break;
                case 4:
                    System.out.print("Введіть назву витрати: ");
                    String delName = InputUtil.readLine();
                    expenseService.deleteExpense(delName);
                    break;
                case 5:
                    expenseService.sortByAmount().forEach(System.out::println);
                    break;
                case 6:
                    expenseService.sortByDate().forEach(System.out::println);
                    break;
                case 7:
                    System.out.print("Назва для пошуку: ");
                    String searchName = InputUtil.readLine();
                    System.out.print("Дата для пошуку: ");
                    String searchDate = InputUtil.readLine();
                    List<Expense> results = expenseService.searchExpenses(searchName, searchDate);
                    results.forEach(System.out::println);
                    break;
                case 8:
                    System.exit(0);
                    break;
                default:
                    System.out.println("Невірний вибір.");
            }
        }
    }
}