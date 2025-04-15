package com.example;

import java.util.function.Function;

public class DesignPatterns {

    // 1. Стратегія (Strategy)
    public static void testStrategyPattern() {
        Function<String, String> upperCaseStrategy = String::toUpperCase;
        Function<String, String> lowerCaseStrategy = String::toLowerCase;

        System.out.println("Upper Case: " + applyStrategy("Hello", upperCaseStrategy));
        System.out.println("Lower Case: " + applyStrategy("Hello", lowerCaseStrategy));
    }

    static String applyStrategy(String input, Function<String, String> strategy) {
        return strategy.apply(input);
    }

    // 2. Фабричний метод (Factory Method)
    public static void testFactoryMethodPattern() {
        Product productA = createProduct("A");
        Product productB = createProduct("B");

        System.out.println(productA.getName());  // Product A
        System.out.println(productB.getName());  // Product B
    }

    interface Product {
        String getName();
    }

    static class ConcreteProductA implements Product {
        public String getName() { return "Product A"; }
    }

    static class ConcreteProductB implements Product {
        public String getName() { return "Product B"; }
    }

    public static Product createProduct(String type) {
        if (type.equals("A")) {
            return new ConcreteProductA();
        } else {
            return new ConcreteProductB();
        }
    }

    // 3. Декоратор (Decorator)
    public static void testDecoratorPattern() {
        Function<String, String> base = s -> s;
        Function<String, String> decorated = base
                .andThen(s -> "**" + s + "**")
                .andThen(s -> "[[" + s + "]]");

        System.out.println(decorated.apply("Text"));
    }

    // 4. Навколишнє виконання (Execute Around)
    public static void testExecuteAroundPattern() {
        executeWithResource(resource -> resource.action());
    }

    static void executeWithResource(Consumer<Resource> consumer) {
        try (Resource resource = new Resource()) {
            consumer.accept(resource);
        }
    }

    static class Resource implements AutoCloseable {
        void action() {
            System.out.println("Using resource");
        }

        @Override
        public void close() {
            System.out.println("Closing resource");
        }
    }

    interface Consumer<T> {
        void accept(T t);
    }
}