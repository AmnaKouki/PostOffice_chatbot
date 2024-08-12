import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import {
  NbChatModule,
  NbLayoutModule,
  NbThemeModule,
  NbButtonModule,
  NbListModule,
} from '@nebular/theme';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HttpClientModule } from '@angular/common/http';

import { TableModule } from 'primeng/table';
import { TimelineModule } from 'primeng/timeline';
import { CardModule } from 'primeng/card';
import { AccordionModule } from 'primeng/accordion';
import { EmbeddedComponent } from './embedded/embedded.component';
import { ChatbotComponent } from './chatbot/chatbot.component';
@NgModule({
  declarations: [AppComponent, EmbeddedComponent, ChatbotComponent],
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
    NbListModule,
    AccordionModule,
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
