import React from 'react'
import { FilmsQuery } from '../../generated/graphql'
// import { Actor, FilmsQuery, Maybe } from '../../generated/graphql'
import { Card, Container} from 'react-bootstrap'
import Collapsible from '../Collapsible';

interface MovieListProps {
    data: FilmsQuery;
}

function truncate(txt: string, length: number) {
    if (txt.length > length) {
        return txt.slice(0, length) + '...';
    } else {
        return txt;
    }
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
                /* let descriptionElement: JSX.Element;
                if (film.description == null) {
                    descriptionElement = <div>No description</div>
                } else {
                    descriptionElement = <Collapsible title="description">
                            {truncate(film.description, 20)}
                        </Collapsible>

                }*/
                ret.push(

                    <Card key={film.id} className="mb-2">
                        <Card.Title>{film.title}</Card.Title>
                        <Card.Body>
                        {/* {descriptionElement} */}
                        <Collapsible title="description">
                            {truncate(film.description, 20)}
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
