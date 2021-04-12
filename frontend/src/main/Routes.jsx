import React from 'react';
import { Redirect } from 'react-router';
import { Route, HashRouter} from 'react-router-dom';

import Polos from '../components/template/Polos';

const routes = (props) => (
    <HashRouter>
        <Route path='/polos' component={Polos}></Route>
        <Redirect from="*" to="/polos" />
    </HashRouter>
)

export default routes;
