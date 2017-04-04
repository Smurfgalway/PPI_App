import { Component, ViewChild } from '@angular/core';
import { NavController } from 'ionic-angular';
import { Geolocation} from 'ionic-native';

declare var google;

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
    
    Geolocation.getCurrentPosition().then((position) => {
 
      let latLng = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);

    let mapOptions = {
      center: latLng,
      zoom: 17,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    }
   
    
  
    this.map = new google.maps.Map(this.mapElement.nativeElement, mapOptions);
    });
  }
  addMarker(){
 
  let marker = new google.maps.Marker({
    map: this.map,
    animation: google.maps.Animation.DROP,
    position: this.map.getCenter()
  });
 
  let content = "dropping a marker";          
 
  this.addInfoWindow(marker, content);
 
}
addInfoWindow(marker, content){
 
  let infoWindow = new google.maps.InfoWindow({
    content: content
  });
 
  google.maps.event.addListener(marker, 'click', () => {
    infoWindow.open(this.map, marker);
  });
 
}
}