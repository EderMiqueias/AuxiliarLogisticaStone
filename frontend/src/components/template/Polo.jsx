import React from 'react';
import Dialog from './PoloDialog'

class Polo extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            url: props.url,
            estoque: props.estoque,
            average: props.average,
            base: props.base,
            color: this.getColorByStockDuration(
                props.estoque,
                props.average
            ),
            ideal: this.getIdealTerminals(
                props.estoque,
                props.average
            ),
        }
    }

    childExpedir = (terms_expedidos) => {
        this.addEstoque(terms_expedidos);
        this.setColor();
        this.setIdeal();
    }

    addEstoque = (terms_expedidos) => {
        this.setState({
            estoque: this.state.estoque + parseInt(terms_expedidos)
        });
    }

    setColor = () => {
        this.setState({
            ...this.state,
            color: this.getColorByStockDuration(
                this.state.estoque,
                this.state.average
            )
        });
    }

    setIdeal = () => {
        this.setState({
            ...this.state,
            ideal: this.getIdealTerminals(
                this.state.estoque,
                this.state.average
            )
        });
    }

    getIdealTerminals(estoque, media) {
        let ideal = media * 14;
        return Math.ceil(ideal - estoque);
    }
    
    getColorByStockDuration(estoque, media) {
        let diasRestantes = estoque / media;
    
        // Cobertura Ideal
        if (diasRestantes >= 14 && diasRestantes <= 18) {
            return "#42EC9A";
        }
        // Atenção
        else if (diasRestantes >= 10 && diasRestantes <= 23) {
            return "#DFFF00";
        }
        // Perigo
        else {
            return "#DE3163";
        }
    }

    render() {
        return (
            <div
                className="Card Polo"
                style={{ borderColor: this.state.color }}
            >
                <div className="Content">
                    <h4>{this.state.base}</h4>
                    <ul>
                        <li>Estoque: {this.state.estoque} terminais</li>
                        <li>Média diária: {this.state.average.toFixed(2)} terminais</li>
                    </ul>
                    <Dialog
                        base={this.state.base}
                        terminais={this.state.estoque}
                        ideal={this.state.ideal}
                        url={this.state.url}
                        childExpedir={this.childExpedir}
                    />
                </div>
            </div>
        );
    }
}

export default Polo;
