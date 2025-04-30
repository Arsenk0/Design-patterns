package org.example.di;

import dagger.internal.DaggerGenerated;
import dagger.internal.Factory;
import dagger.internal.Preconditions;
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
public final class AppModule_ProvideJsonStorageFactory implements Factory<JsonStorage> {
  private final AppModule module;

  public AppModule_ProvideJsonStorageFactory(AppModule module) {
    this.module = module;
  }

  @Override
  public JsonStorage get() {
    return provideJsonStorage(module);
  }

  public static AppModule_ProvideJsonStorageFactory create(AppModule module) {
    return new AppModule_ProvideJsonStorageFactory(module);
  }

  public static JsonStorage provideJsonStorage(AppModule instance) {
    return Preconditions.checkNotNullFromProvides(instance.provideJsonStorage());
  }
}
