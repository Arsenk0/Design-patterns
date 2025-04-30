package org.example.service;

import dagger.internal.DaggerGenerated;
import dagger.internal.Factory;
import dagger.internal.Provider;
import dagger.internal.QualifierMetadata;
import dagger.internal.ScopeMetadata;
import javax.annotation.Generated;
import org.example.storage.JsonStorage;

@ScopeMetadata
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
public final class ExpenseService_Factory implements Factory<ExpenseService> {
  private final Provider<JsonStorage> jsonStorageProvider;

  public ExpenseService_Factory(Provider<JsonStorage> jsonStorageProvider) {
    this.jsonStorageProvider = jsonStorageProvider;
  }

  @Override
  public ExpenseService get() {
    return newInstance(jsonStorageProvider.get());
  }

  public static ExpenseService_Factory create(Provider<JsonStorage> jsonStorageProvider) {
    return new ExpenseService_Factory(jsonStorageProvider);
  }

  public static ExpenseService newInstance(JsonStorage jsonStorage) {
    return new ExpenseService(jsonStorage);
  }
}
