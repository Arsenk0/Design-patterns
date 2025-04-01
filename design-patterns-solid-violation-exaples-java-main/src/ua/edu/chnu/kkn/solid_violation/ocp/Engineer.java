package ua.edu.chnu.kkn.solid_violation.ocp;

public class Engineer extends Employee {

    Engineer(int salary) {
        super(salary, 0);
    }

    @Override
    public int payAmount() {
        return salary;
    }
}