import React from 'react';
import { Button, Collapse } from 'react-bootstrap';

interface CollapsibleProps {
    title: string
}

class Collapsible extends React.Component<CollapsibleProps, {open: boolean}> {
    constructor(props: CollapsibleProps) {
        super(props);
        this.state = {open: false};
        this.setOpen.bind(this);
    }
    render() {
        return (
            <div>
            <Button
                onClick={(event: any) => this.setOpen()}
                aria-controls="{this.id}.collapsible"
                aria-expanded={this.state.open}
            >Show {this.props.title}</Button>
            <Collapse in={this.state.open}>
                <div className="collapsible">
                {this.props.children}
                </div>
            </Collapse>
            </div>
        )
    }

    private setOpen () {
        this.setState((state, props) => {return {open: !this.state.open}});
    }
}

export default Collapsible;