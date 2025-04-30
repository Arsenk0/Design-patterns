package org.example.di;

import dagger.Component;
import org.example.Main;

import javax.inject.Singleton;

@Singleton
@Component(modules = {AppModule.class})
public interface AppComponent {
    void inject(Main main);
}
