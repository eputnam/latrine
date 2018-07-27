import axios from 'axios';

export const getRestrooms = setState => {
    axios
        .get(
            'https://www.refugerestrooms.org:443/api/v1/restrooms/search.json?per_page=100&query=portland',
        )
        .then(response => {
            console.log(response.data);
            const ingressData = reshapeRestroomData(response.data);
            return setState({ restrooms: ingressData });
        });
};

const reshapeRestroomData = restroomArray => {
    // Items are reshaped to a map to easily access later by restroom ID
    const reshapedItems = restroomArray.reduce((acc, item) => {
        return {
            ...acc,
            [item.id]: item,
        };
    }, {});

    // A sorted array of ID's for faster computation when only needing partial data from a restroom
    const sorted = restroomArray
        .map(item => {
            return item.id;
        })
        .sort();

    return {
        items: reshapedItems,
        sort: sorted,
        selected: '',
    };
};
