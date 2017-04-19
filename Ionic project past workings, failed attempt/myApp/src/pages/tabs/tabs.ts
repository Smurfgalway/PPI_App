import { Component } from '@angular/core';

import { HomePage } from '../home/home';
import { mHubPage } from '../Hub1/mHub';
import { sHubPage } from '../Hub2/sHub';

@Component({
  templateUrl: 'tabs.html'
})
export class TabsPage {
  // this tells the tabs component which Pages
  // should be each tab's root Page
  tab1Root: any = HomePage;
  tab2Root: any = mHubPage;
  tab3Root: any = sHubPage;
  constructor() {

  }
}
