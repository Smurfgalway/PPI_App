import { Component, ViewChild } from '@angular/core';

import { NavController } from 'ionic-angular';

@Component({
  selector: 'page-sHub',
  templateUrl: 'sHub.html'
})
export class sHubPage {

  @ViewChild('map') mapElement; 
  map: any;
  constructor(public navCtrl: NavController) {

  }
  ionViewDidLoad(){
    this.initmap();
  }

  
  initmap(){
    let latlng = new google.maps.latLng(Geolocation);

    let mapOptions = {
      center: latlng,
      zoom: 15,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    };
  
    this.map = new google.maps.Map(this.mapElement.nativeElement, mapOptions);
  }
}