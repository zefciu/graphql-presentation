import gql from 'graphql-tag';

export const MOVIE_LIST = gql`query films ($first: Int!) {
  films (first: $first){
    edges {
    	node {
    	    id
            title
            rating
            description
            languageId
            originalLanguageId
            actors {
              edges {
                node {
                  id
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
