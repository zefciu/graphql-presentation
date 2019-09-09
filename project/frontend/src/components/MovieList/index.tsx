import React from 'react'
import { useFilmsQuery } from '../../generated/graphql'
import { MovieList } from './MovieList'

const MovieListContainer = () => {
    const { data, error, loading } = useFilmsQuery({variables:{first: 20}});

    if (loading) {
        return <div>Loading…</div>;
    }

    if (error || !data) {
        return <div>Error</div>;
    }

    return <MovieList data={data} />
};

export {MovieListContainer};