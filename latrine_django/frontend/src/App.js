import React, { Component } from 'react';
import MapContainer from './Map.js';
import Filters from './Filters.js';
import './App.css';

export default class App extends Component {

  constructor() {
    super()
    this.state = {
      restroomsChecked: true
    }
    this.toggleRestrooms = this.toggleRestrooms.bind(this);
  }

  toggleRestrooms() {
    this.setState({
      restroomsChecked: !this.state.restroomsChecked
    });
  }

  render() {
    return (
      <div className="app">
        <Filters restroomsChecked={this.state.restroomsChecked} toggleRestrooms={this.toggleRestrooms} />
        <MapContainer restroomsChecked={this.state.restroomsChecked} />
      </div>
    );
  }
}
