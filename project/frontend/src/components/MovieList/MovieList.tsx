import React from 'react'
import { FilmsQuery, Film } from '../../generated/graphql'

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
            <ol>
                {this.getMovieList()}
            </ol>
        </div>
    }

    private getMovieList(): JSX.Element[] {
        let ret : JSX.Element[] = [] ;
        if (!this.props.data.films) {
            return ret;
        }
        for (let filmEdge of this.props.data.films.edges) {
            console.log(filmEdge);
            if (filmEdge && filmEdge.node) {
                const film = filmEdge.node
                ret.push(<li>{film.title}, {film.description}</li>);
            }
        }
        return ret;
    }
}
