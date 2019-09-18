import React from 'react'
import { FilmsQuery } from '../../generated/graphql'
// import { Actor, FilmsQuery, Maybe } from '../../generated/graphql'
import { Card, Container} from 'react-bootstrap'
import Collapsible from '../Collapsible';

interface MovieListProps {
    data: FilmsQuery;
}

export class MovieList extends React.Component<MovieListProps> {

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
                        <Collapsible title="description">
                            {film.description}
                        </Collapsible>
                        {/*<Collapsible title="actors">
                            <ul>
                            {this.getActors(film.actors)}
                            </ul>
                        </Collapsible>*/}
                        </Card.Body>
                    </Card>
                );

            }
        }
        return ret;
    }

    /* private getActors(
        actors: Maybe<{
            'edges': Maybe<{
                'node': Maybe<Pick<Actor, | 'firstName' | 'lastName'>>
               }>[]
         }>) {
        let ret : JSX.Element[] = [] ;
        if (!actors || !actors.edges) {
            return ret;
        }
        for (let actorEdge of actors.edges) {
            if (!actorEdge || !actorEdge.node) {
                continue;
            }
            let actor = actorEdge.node;
            ret.push(
                <li>{actor.firstName} {actor.lastName}</li>
            )
        }
        return ret;

    } */
}
