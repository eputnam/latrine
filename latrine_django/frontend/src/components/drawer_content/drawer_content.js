import React from 'react';

export default class DrawerContent extends React.Component {
    render() {
        console.log('restroom props: ', this.props.restrooms);
        return <div>Drawer</div>;
    }
}
