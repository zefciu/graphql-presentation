import React from 'react'
import { FilmsQuery, Film } from '../../generated/graphql'
import { Card, Container} from 'react-bootstrap'
import Collapsible from '../Collapsible';

interface MovieListProps {
    data: FilmsQuery;
}

export class MovieList extends React.Component<MovieListProps> {
    constructor(props: MovieListProps) {
        super(props)
    }

    render(): JSX.Element {
        return <div>
            <h1>Movies</h1>
            <Container>
                {this.getMovieList()}
            </Container>
        </div>
    }

    private getMovieList(): JSX.Element[] {
        let ret : JSX.Element[] = [] ;
        if (!this.props.data.films) {
            return ret;
        }
        for (let filmEdge of this.props.data.films.edges) {
            if (filmEdge && filmEdge.node) {
                const film = filmEdge.node
                ret.push(
                    <Card key={film.id} className="mb-2">
                        <Card.Title>{film.title}</Card.Title>
                        <Card.Body>
                        <Collapsible title="opis">
                            {film.description}
                        </Collapsible>
                        </Card.Body>
                    </Card>
                );

            }
        }
        return ret;
    }
}
