import React, { Component } from 'react';
import axios from 'axios';
import { Map, Marker, GoogleApiWrapper } from 'google-maps-react';
import './Map.css';
const pottyImage = require('../../images/potty.png');

export class MapContainer extends Component {
    render() {
        const { restrooms } = this.props;
        return (
            <Map
                google={this.props.google}
                style={{ width: '100%', height: '100%', margin: 'auto' }}
                containerStyle={{
                    width: '100vw',
                    height: '93vh',
                    margin: 'auto',
                }}
                zoom={14}
                initialCenter={{
                    lat: 45.5231,
                    lng: -122.6765,
                }}
            >
                {restrooms.sort.map((restroomId, markerindex) => {
                    const google = window.google;
                    const currentRestroom = restrooms.items[restroomId];
                    const { street, latitude, longitude } = currentRestroom;

                    if (this.props.restroomsChecked) {
                        return (
                            <Marker
                                key={markerindex}
                                onClick={this.props.selectMarker(restroomId)}
                                title={'RefugeRestrooms.org -' + street}
                                name={'RefugeRestrooms.org'}
                                position={{ lat: latitude, lng: longitude }}
                                icon={{
                                    url: pottyImage,
                                    anchor: new google.maps.Point(32, 32),
                                    scaledSize: new google.maps.Size(45, 45),
                                }}
                            />
                        );
                    } else {
                        return null;
                    }
                })}
            </Map>
        );
    }
}

export default GoogleApiWrapper({
    apiKey: 'AIzaSyCxZwna2Pr9JMOm1mUZC1iSMjiWaegroHo',
    version: '3.31',
})(MapContainer);
