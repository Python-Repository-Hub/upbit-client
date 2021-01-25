=begin
#Upbit Open API

### REST API for Upbit Exchange - Base URL: [https://api.upbit.com] - Official Upbit API Documents: [https://docs.upbit.com] - Official Support email: [open-api@upbit.com] 

OpenAPI spec version: 1.0.0
Contact: ujhin942@gmail.com
Generated by: https://github.com/swagger-api/swagger-codegen.git
Swagger Codegen version: 2.4.18

=end

require 'spec_helper'
require 'json'

# Unit tests for SwaggerClient::OrderApi
# Automatically generated by swagger-codegen (github.com/swagger-api/swagger-codegen)
# Please update as you see appropriate
describe 'OrderApi' do
  before do
    # run before each test
    @instance = SwaggerClient::OrderApi.new
  end

  after do
    # run after each test
  end

  describe 'test an instance of OrderApi' do
    it 'should create an instance of OrderApi' do
      expect(@instance).to be_instance_of(SwaggerClient::OrderApi)
    end
  end

  # unit tests for order_cancel
  # 주문 취소 접수
  # ## 주문 UUID를 통해 해당 주문에 대한 취소 접수를 한다. **NOTE**: &#x60;uuid&#x60; 혹은 &#x60;identifier&#x60; 둘 중 하나의 값이 반드시 포함되어야 합니다. 
  # @param [Hash] opts the optional parameters
  # @option opts [String] :uuid 취소할 주문의 UUID 
  # @option opts [String] :identifier 조회용 사용자 지정 값 
  # @return [Order]
  describe 'order_cancel test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for order_chance
  # 주문 가능 정보
  # ## 마켓별 주문 가능 정보를 확인한다. 
  # @param market Market ID 
  # @param [Hash] opts the optional parameters
  # @return [OrderChance]
  describe 'order_chance test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for order_info
  # 개별 주문 조회
  # ## 주문 UUID를 통해 개별 주문건을 조회한다. **NOTE**: &#x60;uuid&#x60; 혹은 &#x60;identifier&#x60; 둘 중 하나의 값이 반드시 포함되어야 합니다. 
  # @param [Hash] opts the optional parameters
  # @option opts [String] :uuid 주문 UUID 
  # @option opts [String] :identifier 조회용 사용자 지정 값 
  # @return [OrderInfo]
  describe 'order_info test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for order_info_all
  # 주문 리스트 조회
  # ## 주문 리스트를 조회한다. 
  # @param [Hash] opts the optional parameters
  # @option opts [String] :market 마켓 아이디 
  # @option opts [String] :state 주문 상태   - wait : 체결 대기 (default)   - done : 전체 체결 완료   - cancel : 주문 취소 
  # @option opts [Array<String>] :states 주문 상태의 목록 
  # @option opts [Array<String>] :uuids 주문 UUID의 목록 
  # @option opts [Array<String>] :identifiers 주문 identifier의 목록 
  # @option opts [Float] :page 페이지 수, default: 1 
  # @option opts [Float] :limit 요청 개수, default: 100 
  # @option opts [String] :order_by 정렬 방식 - asc : 오름차순 - desc : 내림차순 (default) 
  # @return [Array<Order>]
  describe 'order_info_all test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for order_new
  # 주문하기
  # ## 주문 요청을 한다. **NOTE**: 원화 마켓 가격 단위를 확인하세요. 원화 마켓에서 주문을 요청 할 경우, [원화 마켓 주문 가격 단위](https://docs.upbit.com/docs/market-info-trade-price-detail)를 확인하여 값을 입력해주세요. **NOTE**: identifier 파라미터 사용 &#x60;identifier&#x60;는 서비스에서 발급하는 &#x60;uuid&#x60;가 아닌 이용자가 직접 발급하는 키값으로, 주문을 조회하기 위해 할당하는 값입니다. 해당 값은 사용자의 전체 주문 내 유일한 값을 전달해야하며, 비록 주문 요청시 오류가 발생하더라도 같은 값으로 다시 요청을 보낼 수 없습니다. 주문의 성공 / 실패 여부와 관계없이 중복해서 들어온 &#x60;identifier&#x60; 값에서는 중복 오류가 발생하니, 매 요청시 새로운 값을 생성해주세요. **NOTE**: 시장가 주문 시장가 주문은 &#x60;ord_type&#x60; 필드를 &#x60;price&#x60; or &#x60;market&#x60; 으로 설정해야됩니다. 매수 주문의 경우 &#x60;ord_type&#x60;을 &#x60;price&#x60;로 설정하고 &#x60;volume&#x60;을 &#x60;null&#x60; 혹은 제외해야됩니다. 매도 주문의 경우 &#x60;ord_type&#x60;을 &#x60;market&#x60;로 설정하고 &#x60;price&#x60;을 &#x60;null&#x60; 혹은 제외해야됩니다. 
  # @param market 마켓 ID (필수) 
  # @param side 주문 종류 (필수) - bid : 매수 - ask : 매도 
  # @param ord_type 주문 타입 (필수) - limit : 지정가 주문 - price : 시장가 주문(매수) - market : 시장가 주문(매도) 
  # @param [Hash] opts the optional parameters
  # @option opts [String] :volume 주문량 (지정가, 시장가 매도 시 필수) 
  # @option opts [String] :price 주문 가격. (지정가, 시장가 매수 시 필수) ex) KRW-BTC 마켓에서 1BTC당 1,000 KRW로 거래할 경우, 값은 1000 이 된다. ex) KRW-BTC 마켓에서 1BTC당 매도 1호가가 500 KRW 인 경우, 시장가 매수 시 값을 1000으로 세팅하면 2BTC가 매수된다. (수수료가 존재하거나 매도 1호가의 수량에 따라 상이할 수 있음) 
  # @option opts [String] :identifier 조회용 사용자 지정값 (선택) 
  # @return [NewOrder]
  describe 'order_new test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for order_orderbook
  # 시세 호가 정보(Orderbook) 조회
  # ## 호가 정보 조회 
  # @param markets 마켓 코드 목록 (ex. KRW-BTC,KRW-ADA) 
  # @param [Hash] opts the optional parameters
  # @return [Array<Orderbook>]
  describe 'order_orderbook test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

end
