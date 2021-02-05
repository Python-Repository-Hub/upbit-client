# coding: utf-8

"""
    Upbit Open API

    ## REST API for Upbit Exchange - Base URL: [https://api.upbit.com] - Official Upbit API Documents: [https://docs.upbit.com] - Official Support email: [open-api@upbit.com]   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: ujhin942@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class OrderApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def order_cancel(self, **kwargs):  # noqa: E501
        """주문 취소 접수  # noqa: E501

        ## 주문 UUID를 통해 해당 주문에 대한 취소 접수를 한다.  **NOTE**: `uuid` 혹은 `identifier` 둘 중 하나의 값이 반드시 포함되어야 합니다.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.order_cancel(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: 취소할 주문의 UUID 
        :param str identifier: 조회용 사용자 지정 값 
        :return: Order
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.order_cancel_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.order_cancel_with_http_info(**kwargs)  # noqa: E501
            return data

    def order_cancel_with_http_info(self, **kwargs):  # noqa: E501
        """주문 취소 접수  # noqa: E501

        ## 주문 UUID를 통해 해당 주문에 대한 취소 접수를 한다.  **NOTE**: `uuid` 혹은 `identifier` 둘 중 하나의 값이 반드시 포함되어야 합니다.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.order_cancel_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: 취소할 주문의 UUID 
        :param str identifier: 조회용 사용자 지정 값 
        :return: Order
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid', 'identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method order_cancel" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'uuid' in params:
            query_params.append(('uuid', params['uuid']))  # noqa: E501
        if 'identifier' in params:
            query_params.append(('identifier', params['identifier']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/order', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Order',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def order_chance(self, market, **kwargs):  # noqa: E501
        """주문 가능 정보  # noqa: E501

        ## 마켓별 주문 가능 정보를 확인한다.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.order_chance(market, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str market: Market ID  (required)
        :return: OrderChance
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.order_chance_with_http_info(market, **kwargs)  # noqa: E501
        else:
            (data) = self.order_chance_with_http_info(market, **kwargs)  # noqa: E501
            return data

    def order_chance_with_http_info(self, market, **kwargs):  # noqa: E501
        """주문 가능 정보  # noqa: E501

        ## 마켓별 주문 가능 정보를 확인한다.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.order_chance_with_http_info(market, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str market: Market ID  (required)
        :return: OrderChance
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['market']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method order_chance" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'market' is set
        if ('market' not in params or
                params['market'] is None):
            raise ValueError("Missing the required parameter `market` when calling `order_chance`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'market' in params:
            query_params.append(('market', params['market']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/orders/chance', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OrderChance',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def order_info(self, **kwargs):  # noqa: E501
        """개별 주문 조회  # noqa: E501

        ## 주문 UUID를 통해 개별 주문건을 조회한다.  **NOTE**: `uuid` 혹은 `identifier` 둘 중 하나의 값이 반드시 포함되어야 합니다.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.order_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: 주문 UUID 
        :param str identifier: 조회용 사용자 지정 값 
        :return: OrderInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.order_info_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.order_info_with_http_info(**kwargs)  # noqa: E501
            return data

    def order_info_with_http_info(self, **kwargs):  # noqa: E501
        """개별 주문 조회  # noqa: E501

        ## 주문 UUID를 통해 개별 주문건을 조회한다.  **NOTE**: `uuid` 혹은 `identifier` 둘 중 하나의 값이 반드시 포함되어야 합니다.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.order_info_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: 주문 UUID 
        :param str identifier: 조회용 사용자 지정 값 
        :return: OrderInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid', 'identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method order_info" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'uuid' in params:
            query_params.append(('uuid', params['uuid']))  # noqa: E501
        if 'identifier' in params:
            query_params.append(('identifier', params['identifier']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/order', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OrderInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def order_info_all(self, **kwargs):  # noqa: E501
        """주문 리스트 조회  # noqa: E501

        ## 주문 리스트를 조회한다.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.order_info_all(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str market: 마켓 아이디 
        :param str state: 주문 상태   - wait : 체결 대기 (default)   - done : 전체 체결 완료   - cancel : 주문 취소 
        :param list[str] states: 주문 상태의 목록 
        :param list[str] uuids: 주문 UUID의 목록 
        :param list[str] identifiers: 주문 identifier의 목록 
        :param float page: 페이지 수, default: 1 
        :param float limit: 요청 개수, default: 100 
        :param str order_by: 정렬 방식 - asc : 오름차순 - desc : 내림차순 (default) 
        :return: list[Order]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.order_info_all_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.order_info_all_with_http_info(**kwargs)  # noqa: E501
            return data

    def order_info_all_with_http_info(self, **kwargs):  # noqa: E501
        """주문 리스트 조회  # noqa: E501

        ## 주문 리스트를 조회한다.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.order_info_all_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str market: 마켓 아이디 
        :param str state: 주문 상태   - wait : 체결 대기 (default)   - done : 전체 체결 완료   - cancel : 주문 취소 
        :param list[str] states: 주문 상태의 목록 
        :param list[str] uuids: 주문 UUID의 목록 
        :param list[str] identifiers: 주문 identifier의 목록 
        :param float page: 페이지 수, default: 1 
        :param float limit: 요청 개수, default: 100 
        :param str order_by: 정렬 방식 - asc : 오름차순 - desc : 내림차순 (default) 
        :return: list[Order]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['market', 'state', 'states', 'uuids', 'identifiers', 'page', 'limit', 'order_by']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method order_info_all" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'market' in params:
            query_params.append(('market', params['market']))  # noqa: E501
        if 'state' in params:
            query_params.append(('state', params['state']))  # noqa: E501
        if 'states' in params:
            query_params.append(('states', params['states']))  # noqa: E501
            collection_formats['states'] = 'multi'  # noqa: E501
        if 'uuids' in params:
            query_params.append(('uuids', params['uuids']))  # noqa: E501
            collection_formats['uuids'] = 'multi'  # noqa: E501
        if 'identifiers' in params:
            query_params.append(('identifiers', params['identifiers']))  # noqa: E501
            collection_formats['identifiers'] = 'multi'  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('order_by', params['order_by']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/orders', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Order]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def order_new(self, market, side, ord_type, **kwargs):  # noqa: E501
        """주문하기  # noqa: E501

        ## 주문 요청을 한다.  **NOTE**: 원화 마켓 가격 단위를 확인하세요.  원화 마켓에서 주문을 요청 할 경우, [원화 마켓 주문 가격 단위](https://docs.upbit.com/docs/market-info-trade-price-detail)를 확인하여 값을 입력해주세요.  **NOTE**: identifier 파라미터 사용  `identifier`는 서비스에서 발급하는 `uuid`가 아닌 이용자가 직접 발급하는 키값으로, 주문을 조회하기 위해 할당하는 값입니다. 해당 값은 사용자의 전체 주문 내 유일한 값을 전달해야하며, 비록 주문 요청시 오류가 발생하더라도 같은 값으로 다시 요청을 보낼 수 없습니다.  주문의 성공 / 실패 여부와 관계없이 중복해서 들어온 `identifier` 값에서는 중복 오류가 발생하니, 매 요청시 새로운 값을 생성해주세요.  **NOTE**: 시장가 주문  시장가 주문은 `ord_type` 필드를 `price` or `market` 으로 설정해야됩니다. 매수 주문의 경우 `ord_type`을 `price`로 설정하고 `volume`을 `null` 혹은 제외해야됩니다. 매도 주문의 경우 `ord_type`을 `market`로 설정하고 `price`을 `null` 혹은 제외해야됩니다.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.order_new(market, side, ord_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str market: 마켓 ID (필수)  (required)
        :param str side: 주문 종류 (필수) - bid : 매수 - ask : 매도  (required)
        :param str ord_type: 주문 타입 (필수) - limit : 지정가 주문 - price : 시장가 주문(매수) - market : 시장가 주문(매도)  (required)
        :param str volume: 주문량 (지정가, 시장가 매도 시 필수) 
        :param str price: 주문 가격. (지정가, 시장가 매수 시 필수)  ex) KRW-BTC 마켓에서 1BTC당 1,000 KRW로 거래할 경우, 값은 1000 이 된다. ex) KRW-BTC 마켓에서 1BTC당 매도 1호가가 500 KRW 인 경우, 시장가 매수 시 값을 1000으로 세팅하면 2BTC가 매수된다. (수수료가 존재하거나 매도 1호가의 수량에 따라 상이할 수 있음) 
        :param str identifier: 조회용 사용자 지정값 (선택) 
        :return: NewOrder
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.order_new_with_http_info(market, side, ord_type, **kwargs)  # noqa: E501
        else:
            (data) = self.order_new_with_http_info(market, side, ord_type, **kwargs)  # noqa: E501
            return data

    def order_new_with_http_info(self, market, side, ord_type, **kwargs):  # noqa: E501
        """주문하기  # noqa: E501

        ## 주문 요청을 한다.  **NOTE**: 원화 마켓 가격 단위를 확인하세요.  원화 마켓에서 주문을 요청 할 경우, [원화 마켓 주문 가격 단위](https://docs.upbit.com/docs/market-info-trade-price-detail)를 확인하여 값을 입력해주세요.  **NOTE**: identifier 파라미터 사용  `identifier`는 서비스에서 발급하는 `uuid`가 아닌 이용자가 직접 발급하는 키값으로, 주문을 조회하기 위해 할당하는 값입니다. 해당 값은 사용자의 전체 주문 내 유일한 값을 전달해야하며, 비록 주문 요청시 오류가 발생하더라도 같은 값으로 다시 요청을 보낼 수 없습니다.  주문의 성공 / 실패 여부와 관계없이 중복해서 들어온 `identifier` 값에서는 중복 오류가 발생하니, 매 요청시 새로운 값을 생성해주세요.  **NOTE**: 시장가 주문  시장가 주문은 `ord_type` 필드를 `price` or `market` 으로 설정해야됩니다. 매수 주문의 경우 `ord_type`을 `price`로 설정하고 `volume`을 `null` 혹은 제외해야됩니다. 매도 주문의 경우 `ord_type`을 `market`로 설정하고 `price`을 `null` 혹은 제외해야됩니다.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.order_new_with_http_info(market, side, ord_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str market: 마켓 ID (필수)  (required)
        :param str side: 주문 종류 (필수) - bid : 매수 - ask : 매도  (required)
        :param str ord_type: 주문 타입 (필수) - limit : 지정가 주문 - price : 시장가 주문(매수) - market : 시장가 주문(매도)  (required)
        :param str volume: 주문량 (지정가, 시장가 매도 시 필수) 
        :param str price: 주문 가격. (지정가, 시장가 매수 시 필수)  ex) KRW-BTC 마켓에서 1BTC당 1,000 KRW로 거래할 경우, 값은 1000 이 된다. ex) KRW-BTC 마켓에서 1BTC당 매도 1호가가 500 KRW 인 경우, 시장가 매수 시 값을 1000으로 세팅하면 2BTC가 매수된다. (수수료가 존재하거나 매도 1호가의 수량에 따라 상이할 수 있음) 
        :param str identifier: 조회용 사용자 지정값 (선택) 
        :return: NewOrder
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['market', 'side', 'ord_type', 'volume', 'price', 'identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method order_new" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'market' is set
        if ('market' not in params or
                params['market'] is None):
            raise ValueError("Missing the required parameter `market` when calling `order_new`")  # noqa: E501
        # verify the required parameter 'side' is set
        if ('side' not in params or
                params['side'] is None):
            raise ValueError("Missing the required parameter `side` when calling `order_new`")  # noqa: E501
        # verify the required parameter 'ord_type' is set
        if ('ord_type' not in params or
                params['ord_type'] is None):
            raise ValueError("Missing the required parameter `ord_type` when calling `order_new`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'market' in params:
            form_params.append(('market', params['market']))  # noqa: E501
        if 'side' in params:
            form_params.append(('side', params['side']))  # noqa: E501
        if 'volume' in params:
            form_params.append(('volume', params['volume']))  # noqa: E501
        if 'price' in params:
            form_params.append(('price', params['price']))  # noqa: E501
        if 'ord_type' in params:
            form_params.append(('ord_type', params['ord_type']))  # noqa: E501
        if 'identifier' in params:
            form_params.append(('identifier', params['identifier']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded', 'multipart/form-data', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/orders', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NewOrder',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def order_orderbook(self, markets, **kwargs):  # noqa: E501
        """시세 호가 정보(Orderbook) 조회  # noqa: E501

        ## 호가 정보 조회   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.order_orderbook(markets, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] markets: 마켓 코드 목록 (ex. KRW-BTC,KRW-ADA)  (required)
        :return: list[Orderbook]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.order_orderbook_with_http_info(markets, **kwargs)  # noqa: E501
        else:
            (data) = self.order_orderbook_with_http_info(markets, **kwargs)  # noqa: E501
            return data

    def order_orderbook_with_http_info(self, markets, **kwargs):  # noqa: E501
        """시세 호가 정보(Orderbook) 조회  # noqa: E501

        ## 호가 정보 조회   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.order_orderbook_with_http_info(markets, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] markets: 마켓 코드 목록 (ex. KRW-BTC,KRW-ADA)  (required)
        :return: list[Orderbook]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['markets']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method order_orderbook" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'markets' is set
        if ('markets' not in params or
                params['markets'] is None):
            raise ValueError("Missing the required parameter `markets` when calling `order_orderbook`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'markets' in params:
            query_params.append(('markets', params['markets']))  # noqa: E501
            collection_formats['markets'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/orderbook', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Orderbook]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
