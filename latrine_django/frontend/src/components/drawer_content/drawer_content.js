import React from 'react';

export default class DrawerContent extends React.Component {
    render() {
        const {
            selectedRestroomData: { name },
        } = this.props;
        return <div>{name}</div>;
    }
}
