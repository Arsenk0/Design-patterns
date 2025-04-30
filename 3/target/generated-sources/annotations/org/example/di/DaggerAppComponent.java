package org.example.di;

import com.google.errorprone.annotations.CanIgnoreReturnValue;
import dagger.internal.DaggerGenerated;
import dagger.internal.Preconditions;
import javax.annotation.Generated;
import org.example.Main;
import org.example.Main_MembersInjector;
import org.example.service.ExpenseService;

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
public final class DaggerAppComponent {
  private DaggerAppComponent() {
  }

  public static Builder builder() {
    return new Builder();
  }

  public static AppComponent create() {
    return new Builder().build();
  }

  public static final class Builder {
    private AppModule appModule;

    private Builder() {
    }

    public Builder appModule(AppModule appModule) {
      this.appModule = Preconditions.checkNotNull(appModule);
      return this;
    }

    public AppComponent build() {
      if (appModule == null) {
        this.appModule = new AppModule();
      }
      return new AppComponentImpl(appModule);
    }
  }

  private static final class AppComponentImpl implements AppComponent {
    private final AppModule appModule;

    private final AppComponentImpl appComponentImpl = this;

    AppComponentImpl(AppModule appModuleParam) {
      this.appModule = appModuleParam;

    }

    ExpenseService expenseService() {
      return new ExpenseService(AppModule_ProvideJsonStorageFactory.provideJsonStorage(appModule));
    }

    @Override
    public void inject(Main main) {
      injectMain(main);
    }

    @CanIgnoreReturnValue
    private Main injectMain(Main instance) {
      Main_MembersInjector.injectExpenseService(instance, expenseService());
      return instance;
    }
  }
}
