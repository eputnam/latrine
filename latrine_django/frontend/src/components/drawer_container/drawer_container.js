import React from 'react';
import Drawer from '@material-ui/core/Drawer';
import DrawerContent from '../drawer_content/drawer_content';

export default class DrawerContainer extends React.Component {
    render() {
        const {
            restrooms,
            isDrawerOpen,
            toggleDrawer,
            selectedRestroomId,
        } = this.props;

        const hasRestrooms = restrooms.sort.length > 0;
        const selectedRestroomData =
            hasRestrooms && selectedRestroomId
                ? restrooms.items[selectedRestroomId]
                : null;

        return (
            <Drawer open={isDrawerOpen} onClose={toggleDrawer(false)}>
                <div
                    tabIndex={0}
                    role="button"
                    onClick={toggleDrawer(false)}
                    onKeyDown={toggleDrawer(false)}
                >
                    <DrawerContent
                        restrooms={restrooms}
                        selectedRestroomData={selectedRestroomData}
                    />
                </div>
            </Drawer>
        );
    }
}
