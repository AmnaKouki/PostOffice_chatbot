import { Component, inject } from '@angular/core';
import { ChatbotService } from './chatbot.service';
import { v4 as uuidv4 } from 'uuid';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent {
  senderId = '';
  constructor() {
    this.senderId = uuidv4();
  }

  isLoading = false;
  tableCols : any;
  timeTable: any[] = [];
  messages: any[] = [
    {
      text: 'أهلا بيك ! أنا صديقك الChatbot 🤖 . إنجم نعاوك في كل شي يخص خدمات البريد التونسي. كان عندك سؤال تفضل 😊',
      date: new Date(),
      files: '',
      reply: false,
      user: {
        name: 'Bot',
        avatar: 'assets/robot.png',
      },
    },

    {
      date: new Date(),
      type: 'buttons',
      reply: false,
      user: {
        name: 'Bot',
        avatar: 'assets/robot.png',
      },
    },
  ];

  chatbotService = inject(ChatbotService);

  clearMessages() {
    this.messages = [
      {
        text: 'أهلا بيك ! أنا صديقك الChatbot 🤖 . إنجم نعاوك في كل شي يخص خدمات البريد التونسي. كان عندك سؤال تفضل 😊',
        date: new Date(),
        files: '',
        reply: false,
        user: {
          name: 'Bot',
          avatar: 'assets/robot.png',
        },
      },

      {
        date: new Date(),
        type: 'buttons',
        reply: false,
        user: {
          name: 'Bot',
          avatar: 'assets/robot.png',
        },
      },
    ];
  }

  sendMessage(event: any) {
    if (this.isLoading) {
      return;
    }
    // check for super commands
    if (event.message === '/clear') {
      this.clearMessages();
      return;
    }
    this.isLoading = true;

    this.messages.push({
      text: event.message,
      date: new Date(),
      reply: true,
      user: {
        name: 'John Doe',
        avatar: 'assets/robot.png',
      },
    });

    // add loading message
    this.messages.push({
      type: 'loading',
      reply: false,
      user: {
        name: 'Bot',
        avatar: 'assets/robot.png',
      },
    });

    this.chatbotService.sendMessage(event.message, this.senderId).subscribe(
      (data: any) => {
        if (data.length === 0) {
          this.messages.push({
            text: 'سامحني صارت مشكلة ... 😓 كان تنجم تعاود تسأل مرة أخرى',
            date: new Date(),
            reply: false,
            user: {
              name: 'Bot',
              avatar: 'assets/robot.png',
            },
          });
          this.isLoading = false;
          // remove loading message
          this.messages = this.messages.filter(
            (message) => message.type !== 'loading'
          );
          return;
        }

        data.forEach((line: any) => {
          // for each message

          // remove loading message
          this.messages = this.messages.filter(
            (message) => message.type !== 'loading'
          );
          // change loading state to false
          this.isLoading = false;

          // check message type
          // TEXT
          if (line.image) {
            this.messages.push({
              type: 'file',
              date: new Date(),
              reply: false,
              user: {
                name: 'Bot',
                avatar: 'assets/robot.png',
              },
              files: [
                {
                  url: line.image,
                  type: 'image/jpeg',
                },
              ],
            });
          }
          if (line.text) {
            this.messages.push({
              text: line.text,
              date: new Date(),
              reply: false,
              user: {
                name: 'Bot',
                avatar: 'assets/robot.png',
              },
            });
          }
          if (line.custom?.tracking) {
            this.items = line.custom.items;
            this.messages.push({
              date: new Date(),
              type: 'steps',
              reply: false,
              user: {
                name: 'Bot',
                avatar: 'assets/robot.png',
              },
            });
          }
          if (line.custom?.workHoursTable){
            this.tableCols = [
              { field: 'day', header: 'اليوم' },
              { field: 'time', header: 'التوقيت' }
            ];
            this.timeTable= line.custom.workingHours;

            this.messages.push({
              date: new Date(),
              reply: false,
              type: 'workHoursTable',
              user: {
                name: 'Bot',
                avatar: 'assets/robot.png',
              },
            });
          }
          if (line.custom?.workHoursButtons) {
            this.messages.push({
              date: new Date(),
              type: 'workHoursBtn',
              reply: false,
              user: {
                name: 'Bot',
                avatar: 'assets/robot.png',
              },
            });
          
          
          }
           
        });




        this.scrollDown();
      },
      (err) => {
        this.messages.push({
          text: 'سامحني صارت مشكلة ... 😓 كان تنجم تعاود تسأل مرة أخرى',
          date: new Date(),
          reply: false,
          user: {
            name: 'Bot',
            avatar: 'assets/robot.png',
          },
        });
        this.isLoading = false;
        // remove loading message
        this.messages = this.messages.filter(
          (message) => message.type !== 'loading'
        );
      }
    );
  }

  isStringContainsArabic(str: string) {
    const arabic = /[\u0600-\u06FF]/;
    // return true if arabic and false if it's not
    return arabic.test(str);
  }

  isUserMessageArabic: string = 'rtl';

  handleInputChange(input: any) {
    const isArabic = this.isStringContainsArabic(input[0]);
    if (isArabic) {
      //this.layoutService.setDirection(NbLayoutDirection.RTL)
      // add direction rtl to messageInput
      this.isUserMessageArabic = 'rtl';
    } else {
      // add direction ltr to messageInput
      this.isUserMessageArabic = 'ltr';
      //this.layoutService.setDirection(NbLayoutDirection.LTR)
    }
  }

  forceMessage(message: string) {
    let msgObj = {
      text: message,
      message: message,
      date: new Date(),
      reply: true,
      user: {
        name: 'Bot',
        avatar: 'assets/robot.png',
      },
    };

    this.sendMessage(msgObj);

    this.messages = this.messages.filter(
      (message) => message.type !== 'buttons' && message.type !== 'workHoursBtn'
    );
  }

  scrollDown() {
    // .messages element and scroll down
    const messagesElement = document.querySelector('.messages');

    setTimeout(
      () => messagesElement?.scrollTo(0, messagesElement.scrollHeight),
      500
    );
  }

  // tracking history
  items: any[] = [];
}
