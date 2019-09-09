import gql from 'graphql-tag';

export const MOVIE_LIST = gql`query films ($first: Int!) {
  films (first: $first){
    edges {
    	node {
        title
        rating
        description
        languageId
        originalLanguageId
        actors {
          edges {
            node {
              firstName
              lastName
            }
          }
        }
      }
    }
    pageInfo{
      hasNextPage
      endCursor
    }
  }
}`;
