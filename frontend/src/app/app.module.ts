import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import {
  NbChatModule,
  NbLayoutModule,
  NbThemeModule,
  NbButtonModule,
} from '@nebular/theme';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HttpClientModule } from '@angular/common/http';

import { TableModule } from 'primeng/table';
import { TimelineModule } from 'primeng/timeline';
import { CardModule } from 'primeng/card';


@NgModule({
  declarations: [AppComponent],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NbThemeModule.forRoot(),
    NbChatModule,
    NbLayoutModule,
    BrowserAnimationsModule,
    NbButtonModule,
    HttpClientModule,
    TimelineModule,
    CardModule,
    TableModule,
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
