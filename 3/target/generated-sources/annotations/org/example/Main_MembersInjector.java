package org.example;

import dagger.MembersInjector;
import dagger.internal.DaggerGenerated;
import dagger.internal.InjectedFieldSignature;
import dagger.internal.Provider;
import dagger.internal.QualifierMetadata;
import javax.annotation.Generated;
import org.example.service.ExpenseService;

@QualifierMetadata
@DaggerGenerated
@Generated(
    value = "dagger.internal.codegen.ComponentProcessor",
    comments = "https://dagger.dev"
)
@SuppressWarnings({
    "unchecked",
    "rawtypes",
    "KotlinInternal",
    "KotlinInternalInJava",
    "cast",
    "deprecation",
    "nullness:initialization.field.uninitialized"
})
public final class Main_MembersInjector implements MembersInjector<Main> {
  private final Provider<ExpenseService> expenseServiceProvider;

  public Main_MembersInjector(Provider<ExpenseService> expenseServiceProvider) {
    this.expenseServiceProvider = expenseServiceProvider;
  }

  public static MembersInjector<Main> create(Provider<ExpenseService> expenseServiceProvider) {
    return new Main_MembersInjector(expenseServiceProvider);
  }

  @Override
  public void injectMembers(Main instance) {
    injectExpenseService(instance, expenseServiceProvider.get());
  }

  @InjectedFieldSignature("org.example.Main.expenseService")
  public static void injectExpenseService(Main instance, ExpenseService expenseService) {
    instance.expenseService = expenseService;
  }
}
