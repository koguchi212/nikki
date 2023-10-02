/* tslint:disable */
/* eslint-disable */
/**
 * FastAPI
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


import type { Configuration } from './configuration';
import type { AxiosPromise, AxiosInstance, AxiosRequestConfig } from 'axios';
import globalAxios from 'axios';
// Some imports not used depending on template conditions
// @ts-ignore
import { DUMMY_BASE_URL, assertParamExists, setApiKeyToObject, setBasicAuthToObject, setBearerAuthToObject, setOAuthToObject, setSearchParams, serializeDataIfNeeded, toPathString, createRequestFunction } from './common';
import type { RequestArgs } from './base';
// @ts-ignore
import { BASE_PATH, COLLECTION_FORMATS, BaseAPI, RequiredError } from './base';

/**
 * 
 * @export
 * @interface Blog
 */
export interface Blog {
    /**
     * 
     * @type {string}
     * @memberof Blog
     */
    'title': string;
    /**
     * 
     * @type {string}
     * @memberof Blog
     */
    'body': string;
}
/**
 * 
 * @export
 * @interface HTTPValidationError
 */
export interface HTTPValidationError {
    /**
     * 
     * @type {Array<ValidationError>}
     * @memberof HTTPValidationError
     */
    'detail'?: Array<ValidationError>;
}
/**
 * 
 * @export
 * @interface ShowBlog
 */
export interface ShowBlog {
    /**
     * 
     * @type {string}
     * @memberof ShowBlog
     */
    'title': string;
    /**
     * 
     * @type {string}
     * @memberof ShowBlog
     */
    'body': string;
}
/**
 * 
 * @export
 * @interface ShowUser
 */
export interface ShowUser {
    /**
     * 
     * @type {string}
     * @memberof ShowUser
     */
    'name': string;
    /**
     * 
     * @type {string}
     * @memberof ShowUser
     */
    'email': string;
    /**
     * 
     * @type {Array<Blog>}
     * @memberof ShowUser
     */
    'blogs': Array<Blog>;
}
/**
 * 
 * @export
 * @interface User
 */
export interface User {
    /**
     * 
     * @type {string}
     * @memberof User
     */
    'name': string;
    /**
     * 
     * @type {string}
     * @memberof User
     */
    'email': string;
    /**
     * 
     * @type {string}
     * @memberof User
     */
    'password': string;
}
/**
 * 
 * @export
 * @interface ValidationError
 */
export interface ValidationError {
    /**
     * 
     * @type {Array<ValidationErrorLocInner>}
     * @memberof ValidationError
     */
    'loc': Array<ValidationErrorLocInner>;
    /**
     * 
     * @type {string}
     * @memberof ValidationError
     */
    'msg': string;
    /**
     * 
     * @type {string}
     * @memberof ValidationError
     */
    'type': string;
}
/**
 * 
 * @export
 * @interface ValidationErrorLocInner
 */
export interface ValidationErrorLocInner {
}

/**
 * AuthApi - axios parameter creator
 * @export
 */
export const AuthApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary Login
         * @param {string} username 
         * @param {string} password 
         * @param {string | null} [grantType] 
         * @param {string} [scope] 
         * @param {string | null} [clientId] 
         * @param {string | null} [clientSecret] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        loginLoginPost: async (username: string, password: string, grantType?: string | null, scope?: string, clientId?: string | null, clientSecret?: string | null, options: AxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'username' is not null or undefined
            assertParamExists('loginLoginPost', 'username', username)
            // verify required parameter 'password' is not null or undefined
            assertParamExists('loginLoginPost', 'password', password)
            const localVarPath = `/login`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options};
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;
            const localVarFormParams = new URLSearchParams();


            if (grantType !== undefined) { 
                localVarFormParams.set('grant_type', grantType as any);
            }
    
            if (username !== undefined) { 
                localVarFormParams.set('username', username as any);
            }
    
            if (password !== undefined) { 
                localVarFormParams.set('password', password as any);
            }
    
            if (scope !== undefined) { 
                localVarFormParams.set('scope', scope as any);
            }
    
            if (clientId !== undefined) { 
                localVarFormParams.set('client_id', clientId as any);
            }
    
            if (clientSecret !== undefined) { 
                localVarFormParams.set('client_secret', clientSecret as any);
            }
    
    
            localVarHeaderParameter['Content-Type'] = 'application/x-www-form-urlencoded';
    
            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = {...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers};
            localVarRequestOptions.data = localVarFormParams.toString();

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * AuthApi - functional programming interface
 * @export
 */
export const AuthApiFp = function(configuration?: Configuration) {
    const localVarAxiosParamCreator = AuthApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary Login
         * @param {string} username 
         * @param {string} password 
         * @param {string | null} [grantType] 
         * @param {string} [scope] 
         * @param {string | null} [clientId] 
         * @param {string | null} [clientSecret] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async loginLoginPost(username: string, password: string, grantType?: string | null, scope?: string, clientId?: string | null, clientSecret?: string | null, options?: AxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<void>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.loginLoginPost(username, password, grantType, scope, clientId, clientSecret, options);
            return createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration);
        },
    }
};

/**
 * AuthApi - factory interface
 * @export
 */
export const AuthApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = AuthApiFp(configuration)
    return {
        /**
         * 
         * @summary Login
         * @param {string} username 
         * @param {string} password 
         * @param {string | null} [grantType] 
         * @param {string} [scope] 
         * @param {string | null} [clientId] 
         * @param {string | null} [clientSecret] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        loginLoginPost(username: string, password: string, grantType?: string | null, scope?: string, clientId?: string | null, clientSecret?: string | null, options?: any): AxiosPromise<void> {
            return localVarFp.loginLoginPost(username, password, grantType, scope, clientId, clientSecret, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * AuthApi - object-oriented interface
 * @export
 * @class AuthApi
 * @extends {BaseAPI}
 */
export class AuthApi extends BaseAPI {
    /**
     * 
     * @summary Login
     * @param {string} username 
     * @param {string} password 
     * @param {string | null} [grantType] 
     * @param {string} [scope] 
     * @param {string | null} [clientId] 
     * @param {string | null} [clientSecret] 
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof AuthApi
     */
    public loginLoginPost(username: string, password: string, grantType?: string | null, scope?: string, clientId?: string | null, clientSecret?: string | null, options?: AxiosRequestConfig) {
        return AuthApiFp(this.configuration).loginLoginPost(username, password, grantType, scope, clientId, clientSecret, options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * BlogsApi - axios parameter creator
 * @export
 */
export const BlogsApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * # この関数はすべてのブログを取得します。
         * @summary All Fetch
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        allFetchBlogGet: async (options: AxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/blog/`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options};
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication OAuth2PasswordBearer required
            // oauth required
            await setOAuthToObject(localVarHeaderParameter, "OAuth2PasswordBearer", [], configuration)


    
            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = {...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers};

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * # この関数はブログを作成します。
         * @summary Create
         * @param {Blog} blog 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createBlogPost: async (blog: Blog, options: AxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'blog' is not null or undefined
            assertParamExists('createBlogPost', 'blog', blog)
            const localVarPath = `/blog/`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options};
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication OAuth2PasswordBearer required
            // oauth required
            await setOAuthToObject(localVarHeaderParameter, "OAuth2PasswordBearer", [], configuration)


    
            localVarHeaderParameter['Content-Type'] = 'application/json';

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = {...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers};
            localVarRequestOptions.data = serializeDataIfNeeded(blog, localVarRequestOptions, configuration)

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * # この関数はidでブログを削除します。
         * @summary Delete
         * @param {number} id 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        deleteBlogIdDelete: async (id: number, options: AxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'id' is not null or undefined
            assertParamExists('deleteBlogIdDelete', 'id', id)
            const localVarPath = `/blog/{id}`
                .replace(`{${"id"}}`, encodeURIComponent(String(id)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'DELETE', ...baseOptions, ...options};
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;


    
            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = {...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers};

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * # この関数はidでブログを取得します。
         * @summary Show
         * @param {number} id 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        showBlogIdGet: async (id: number, options: AxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'id' is not null or undefined
            assertParamExists('showBlogIdGet', 'id', id)
            const localVarPath = `/blog/{id}`
                .replace(`{${"id"}}`, encodeURIComponent(String(id)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options};
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;


    
            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = {...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers};

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * # この関数はidでブログを更新します。
         * @summary Update
         * @param {} UNKNOWN_PARAMETER_NAME 
         * @param {Blog} blog 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        updateBlogIdPut: async (UNKNOWN_PARAMETER_NAME: , blog: Blog, options: AxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'UNKNOWN_PARAMETER_NAME' is not null or undefined
            assertParamExists('updateBlogIdPut', 'UNKNOWN_PARAMETER_NAME', UNKNOWN_PARAMETER_NAME)
            // verify required parameter 'blog' is not null or undefined
            assertParamExists('updateBlogIdPut', 'blog', blog)
            const localVarPath = `/blog/{id}`
                .replace(`{${"id"}}`, encodeURIComponent(String(UNKNOWN_PARAMETER_NAME)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'PUT', ...baseOptions, ...options};
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;


    
            localVarHeaderParameter['Content-Type'] = 'application/json';

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = {...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers};
            localVarRequestOptions.data = serializeDataIfNeeded(blog, localVarRequestOptions, configuration)

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * BlogsApi - functional programming interface
 * @export
 */
export const BlogsApiFp = function(configuration?: Configuration) {
    const localVarAxiosParamCreator = BlogsApiAxiosParamCreator(configuration)
    return {
        /**
         * # この関数はすべてのブログを取得します。
         * @summary All Fetch
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async allFetchBlogGet(options?: AxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<Array<ShowBlog>>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.allFetchBlogGet(options);
            return createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration);
        },
        /**
         * # この関数はブログを作成します。
         * @summary Create
         * @param {Blog} blog 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async createBlogPost(blog: Blog, options?: AxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<ShowBlog>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.createBlogPost(blog, options);
            return createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration);
        },
        /**
         * # この関数はidでブログを削除します。
         * @summary Delete
         * @param {number} id 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async deleteBlogIdDelete(id: number, options?: AxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<void>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.deleteBlogIdDelete(id, options);
            return createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration);
        },
        /**
         * # この関数はidでブログを取得します。
         * @summary Show
         * @param {number} id 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async showBlogIdGet(id: number, options?: AxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<ShowBlog>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.showBlogIdGet(id, options);
            return createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration);
        },
        /**
         * # この関数はidでブログを更新します。
         * @summary Update
         * @param {} UNKNOWN_PARAMETER_NAME 
         * @param {Blog} blog 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async updateBlogIdPut(UNKNOWN_PARAMETER_NAME: , blog: Blog, options?: AxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<ShowBlog>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.updateBlogIdPut(UNKNOWN_PARAMETER_NAME, blog, options);
            return createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration);
        },
    }
};

/**
 * BlogsApi - factory interface
 * @export
 */
export const BlogsApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = BlogsApiFp(configuration)
    return {
        /**
         * # この関数はすべてのブログを取得します。
         * @summary All Fetch
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        allFetchBlogGet(options?: any): AxiosPromise<Array<ShowBlog>> {
            return localVarFp.allFetchBlogGet(options).then((request) => request(axios, basePath));
        },
        /**
         * # この関数はブログを作成します。
         * @summary Create
         * @param {Blog} blog 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createBlogPost(blog: Blog, options?: any): AxiosPromise<ShowBlog> {
            return localVarFp.createBlogPost(blog, options).then((request) => request(axios, basePath));
        },
        /**
         * # この関数はidでブログを削除します。
         * @summary Delete
         * @param {number} id 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        deleteBlogIdDelete(id: number, options?: any): AxiosPromise<void> {
            return localVarFp.deleteBlogIdDelete(id, options).then((request) => request(axios, basePath));
        },
        /**
         * # この関数はidでブログを取得します。
         * @summary Show
         * @param {number} id 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        showBlogIdGet(id: number, options?: any): AxiosPromise<ShowBlog> {
            return localVarFp.showBlogIdGet(id, options).then((request) => request(axios, basePath));
        },
        /**
         * # この関数はidでブログを更新します。
         * @summary Update
         * @param {} UNKNOWN_PARAMETER_NAME 
         * @param {Blog} blog 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        updateBlogIdPut(UNKNOWN_PARAMETER_NAME: , blog: Blog, options?: any): AxiosPromise<ShowBlog> {
            return localVarFp.updateBlogIdPut(UNKNOWN_PARAMETER_NAME, blog, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * BlogsApi - object-oriented interface
 * @export
 * @class BlogsApi
 * @extends {BaseAPI}
 */
export class BlogsApi extends BaseAPI {
    /**
     * # この関数はすべてのブログを取得します。
     * @summary All Fetch
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof BlogsApi
     */
    public allFetchBlogGet(options?: AxiosRequestConfig) {
        return BlogsApiFp(this.configuration).allFetchBlogGet(options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * # この関数はブログを作成します。
     * @summary Create
     * @param {Blog} blog 
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof BlogsApi
     */
    public createBlogPost(blog: Blog, options?: AxiosRequestConfig) {
        return BlogsApiFp(this.configuration).createBlogPost(blog, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * # この関数はidでブログを削除します。
     * @summary Delete
     * @param {number} id 
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof BlogsApi
     */
    public deleteBlogIdDelete(id: number, options?: AxiosRequestConfig) {
        return BlogsApiFp(this.configuration).deleteBlogIdDelete(id, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * # この関数はidでブログを取得します。
     * @summary Show
     * @param {number} id 
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof BlogsApi
     */
    public showBlogIdGet(id: number, options?: AxiosRequestConfig) {
        return BlogsApiFp(this.configuration).showBlogIdGet(id, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * # この関数はidでブログを更新します。
     * @summary Update
     * @param {} UNKNOWN_PARAMETER_NAME 
     * @param {Blog} blog 
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof BlogsApi
     */
    public updateBlogIdPut(UNKNOWN_PARAMETER_NAME: , blog: Blog, options?: AxiosRequestConfig) {
        return BlogsApiFp(this.configuration).updateBlogIdPut(UNKNOWN_PARAMETER_NAME, blog, options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * UsersApi - axios parameter creator
 * @export
 */
export const UsersApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * # この関数はユーザーを作成します。
         * @summary Create User
         * @param {User} user 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createUserUserPost: async (user: User, options: AxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'user' is not null or undefined
            assertParamExists('createUserUserPost', 'user', user)
            const localVarPath = `/user/`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options};
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;


    
            localVarHeaderParameter['Content-Type'] = 'application/json';

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = {...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers};
            localVarRequestOptions.data = serializeDataIfNeeded(user, localVarRequestOptions, configuration)

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * # この関数はidでユーザーを削除します。
         * @summary Delete
         * @param {number} id 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        deleteUserIdDelete: async (id: number, options: AxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'id' is not null or undefined
            assertParamExists('deleteUserIdDelete', 'id', id)
            const localVarPath = `/user/{id}`
                .replace(`{${"id"}}`, encodeURIComponent(String(id)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'DELETE', ...baseOptions, ...options};
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;


    
            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = {...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers};

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * # この関数はidでユーザーを取得します。
         * @summary Get User
         * @param {number} id 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getUserUserIdGet: async (id: number, options: AxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'id' is not null or undefined
            assertParamExists('getUserUserIdGet', 'id', id)
            const localVarPath = `/user/{id}`
                .replace(`{${"id"}}`, encodeURIComponent(String(id)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options};
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;


    
            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = {...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers};

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * UsersApi - functional programming interface
 * @export
 */
export const UsersApiFp = function(configuration?: Configuration) {
    const localVarAxiosParamCreator = UsersApiAxiosParamCreator(configuration)
    return {
        /**
         * # この関数はユーザーを作成します。
         * @summary Create User
         * @param {User} user 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async createUserUserPost(user: User, options?: AxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<ShowUser>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.createUserUserPost(user, options);
            return createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration);
        },
        /**
         * # この関数はidでユーザーを削除します。
         * @summary Delete
         * @param {number} id 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async deleteUserIdDelete(id: number, options?: AxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<void>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.deleteUserIdDelete(id, options);
            return createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration);
        },
        /**
         * # この関数はidでユーザーを取得します。
         * @summary Get User
         * @param {number} id 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getUserUserIdGet(id: number, options?: AxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<ShowUser>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getUserUserIdGet(id, options);
            return createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration);
        },
    }
};

/**
 * UsersApi - factory interface
 * @export
 */
export const UsersApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = UsersApiFp(configuration)
    return {
        /**
         * # この関数はユーザーを作成します。
         * @summary Create User
         * @param {User} user 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createUserUserPost(user: User, options?: any): AxiosPromise<ShowUser> {
            return localVarFp.createUserUserPost(user, options).then((request) => request(axios, basePath));
        },
        /**
         * # この関数はidでユーザーを削除します。
         * @summary Delete
         * @param {number} id 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        deleteUserIdDelete(id: number, options?: any): AxiosPromise<void> {
            return localVarFp.deleteUserIdDelete(id, options).then((request) => request(axios, basePath));
        },
        /**
         * # この関数はidでユーザーを取得します。
         * @summary Get User
         * @param {number} id 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getUserUserIdGet(id: number, options?: any): AxiosPromise<ShowUser> {
            return localVarFp.getUserUserIdGet(id, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * UsersApi - object-oriented interface
 * @export
 * @class UsersApi
 * @extends {BaseAPI}
 */
export class UsersApi extends BaseAPI {
    /**
     * # この関数はユーザーを作成します。
     * @summary Create User
     * @param {User} user 
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof UsersApi
     */
    public createUserUserPost(user: User, options?: AxiosRequestConfig) {
        return UsersApiFp(this.configuration).createUserUserPost(user, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * # この関数はidでユーザーを削除します。
     * @summary Delete
     * @param {number} id 
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof UsersApi
     */
    public deleteUserIdDelete(id: number, options?: AxiosRequestConfig) {
        return UsersApiFp(this.configuration).deleteUserIdDelete(id, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * # この関数はidでユーザーを取得します。
     * @summary Get User
     * @param {number} id 
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof UsersApi
     */
    public getUserUserIdGet(id: number, options?: AxiosRequestConfig) {
        return UsersApiFp(this.configuration).getUserUserIdGet(id, options).then((request) => request(this.axios, this.basePath));
    }
}


