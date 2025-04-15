package com.example;

public class Main {
    public static void main(String[] args) {
        System.out.println("Testing Strategy Pattern:");
        DesignPatterns.testStrategyPattern();

        System.out.println("\nTesting Factory Method Pattern:");
        DesignPatterns.testFactoryMethodPattern();

        System.out.println("\nTesting Decorator Pattern:");
        DesignPatterns.testDecoratorPattern();

        System.out.println("\nTesting Execute Around Pattern:");
        DesignPatterns.testExecuteAroundPattern();
    }
}