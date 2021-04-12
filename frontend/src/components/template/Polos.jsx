import React from 'react';

import Polo from './Polo';
import Legend from './Legend'
import api from '../../services/api'

export default class Polos extends React.Component {
    constructor(props) {
        super(props);
        this.state = { list: [] }

        this.refresh();
    }

    refresh() {
        api.get("/polos")
            .then((resp) => {this.setState({
                ...this.state,
                list: resp.data.map((polo) => {
                    return (
                        <Polo
                            key={polo.id}
                            base={polo.base}
                            estoque={polo.estoque}
                            average={polo.average}
                            url={polo.url}
                        />
                    );
                })
            })})
            .catch((err) => {
                console.error("ops! não posso conectar a api " + err);
            });
    }

    render() {
        return (
            <div>
                <div className="header">
                    <h1 className="title">POLOS</h1><br />
                    <h4>Legenda:</h4>
                    <Legend color="#42EC9A" text="COBERTURA IDEAL" />
                    <Legend color="#DFFF00" text="ATENÇÃO" />
                    <Legend color="#DE3163" text="PERIGO" />
                </div>
                <div className="Polos">
                    {this.state.list}
                </div>
            </div>
        );
    }
}
