package org.example.di;

import dagger.Module;
import dagger.Provides;
import org.example.storage.JsonStorage;
//how to create
@Module
public class AppModule {
    @Provides
    JsonStorage provideJsonStorage() {
        return new JsonStorage();
    }
}
