import React, { Component } from 'react';
import MapContainer from './components/map/Map';
import DrawerContainer from './components/drawer_container/drawer_container';
import Filters from './components/filters/Filters';
import { getRestrooms } from './util/restrooms_utils';
import './App.css';

export default class App extends Component {
    constructor() {
        super();
        this.state = {
            restroomsChecked: true,
            isDrawerOpen: false,
            selectedMarker: null,
            restrooms: {
                items: [],
                sort: [],
                selected: '',
            },
        };

        this.toggleRestrooms = this.toggleRestrooms.bind(this);
        this.toggleDrawer = this.toggleDrawer.bind(this);
    }

    componentDidMount() {
        getRestrooms(this.setState.bind(this));
    }

    toggleDrawer = (isOpen = true) => () => {
        this.setState({
            isDrawerOpen: isOpen,
        });
    };

    toggleRestrooms() {
        this.setState({
            restroomsChecked: !this.state.restroomsChecked,
        });
    }

    selectMarker = markerId => () => {
        this.setState({
            selectedMarker: markerId,
            isDrawerOpen: true,
        });
    };

    render() {
        const { restrooms } = this.state;

        return (
            <div className="app">
                <DrawerContainer
                    restrooms={restrooms}
                    toggleDrawer={this.toggleDrawer}
                    isDrawerOpen={this.state.isDrawerOpen}
                    selectedRestroomId={this.state.selectedMarker}
                />
                <Filters
                    restroomsChecked={this.state.restroomsChecked}
                    toggleRestrooms={this.toggleRestrooms}
                />
                <MapContainer
                    restroomsChecked={this.state.restroomsChecked}
                    selectMarker={this.selectMarker}
                    restrooms={restrooms}
                />
            </div>
        );
    }
}
