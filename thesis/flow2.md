# Target Flow Characteristics for DDoS Attacks in SDN

## Data-to-Control Plane Saturation Attack Flow Patterns

### 1. Primary Attack Flow Characteristics

Data-to-control plane saturation attacks in SDN environments typically exhibit the following flow characteristics:

- **Header Field Randomization**: 
  - Randomly generated or spoofed source IP addresses
  - Randomized source port numbers
  - Varying destination ports targeting services on the network
  - Potentially randomized MAC addresses

- **Flow Rule Evasion**:
  - Crafted to avoid matching existing flow rules in switches
  - High probability of causing table-miss events
  - Low probability of aggregation into existing flows
  - Designed to force packet-in messages to the controller

- **Temporal Patterns**:
  - High rate of new flow arrivals
  - Short-lived flows (often single packet)
  - Irregular inter-arrival times to evade rate-based detection
  - Potential for synchronized bursts across multiple sources

- **Spatial Distribution**:
  - Multiple source addresses (often spoofed)
  - Potentially targeting multiple destination addresses
  - Distributed across different ingress points in the network
  - May focus on specific network segments or services

### 2. Attack Variants and Their Flow Characteristics

#### 2.1 Basic Packet Flooding

- **Characteristics**:
  - Simple high-volume packet generation
  - Minimal variation in packet content
  - Consistent packet sizes
  - Regular temporal patterns
  - Easily detectable through volume-based metrics

- **Flow Signatures**:
  - Extremely high packets-per-second rate
  - Low entropy in packet content
  - Uniform packet size distribution
  - Regular inter-arrival times

#### 2.2 Sophisticated Table-Miss Flooding

- **Characteristics**:
  - Carefully crafted packets with randomized fields
  - Varying packet sizes and content
  - Irregular sending patterns
  - Designed to maximize controller processing overhead

- **Flow Signatures**:
  - High entropy in header fields
  - Variable packet sizes
  - Irregular but sustained flow creation rate
  - High ratio of packet-in messages to data plane traffic

#### 2.3 Low-Rate Stealth Attacks

- **Characteristics**:
  - Lower volume to avoid volume-based detection
  - Highly randomized packet fields
  - Irregular timing to avoid pattern detection
  - Potentially mimicking legitimate traffic patterns

- **Flow Signatures**:
  - Moderate packet rates below typical alarm thresholds
  - Very high entropy in header fields
  - Irregular inter-arrival times
  - Sustained over longer periods

#### 2.4 Distributed Coordinated Attacks

- **Characteristics**:
  - Coordinated across multiple sources
  - Synchronized timing or complementary patterns
  - Distributed target selection
  - Potentially adapting to defense mechanisms

- **Flow Signatures**:
  - Correlated activity across multiple ingress points
  - Synchronized flow creation patterns
  - Distributed source address space
  - Potential for attack phase transitions

### 3. Distinguishing Features from Legitimate Traffic

#### 3.1 Protocol Completeness

- **Attack Flows**:
  - Often incomplete protocol exchanges
  - Missing response packets
  - Abnormal protocol state transitions
  - Violation of protocol specifications

- **Legitimate Flows**:
  - Complete protocol handshakes
  - Expected request-response patterns
  - Normal protocol state transitions
  - Adherence to protocol specifications

#### 3.2 Flow Symmetry

- **Attack Flows**:
  - Highly asymmetric (primarily unidirectional)
  - Disproportionate volume in one direction
  - Lack of acknowledgment packets
  - Abnormal request-to-response ratios

- **Legitimate Flows**:
  - Relatively symmetric bidirectional communication
  - Balanced volume in both directions
  - Normal acknowledgment patterns
  - Expected request-to-response ratios

#### 3.3 Flow Duration and Stability

- **Attack Flows**:
  - Often very short-lived
  - Single packet or few packets per flow
  - Lack of established connections
  - High rate of new flow creation

- **Legitimate Flows**:
  - Longer duration
  - Multiple packets per flow
  - Established connections
  - Moderate rate of new flow creation

#### 3.4 Header Field Distribution

- **Attack Flows**:
  - High entropy in source IP addresses
  - Unusual port number distributions
  - Random or invalid flag combinations
  - Potentially malformed headers

- **Legitimate Flows**:
  - Lower entropy in source IP addresses
  - Expected port number distributions
  - Valid flag combinations
  - Well-formed headers

### 4. Target Flow Identification Metrics

#### 4.1 Primary Metrics for Attack Flow Identification

1. **Flow Creation Rate (FCR)**:
   - Number of new flows per second
   - Threshold depends on network size and normal activity
   - Sudden spikes indicate potential attacks
   - Can be measured per switch or network-wide

2. **Packet-In Rate (PIR)**:
   - Number of packet-in messages to controller per second
   - Directly correlates with control plane load
   - Critical indicator of data-to-control plane saturation
   - Can be measured per switch or controller-wide

3. **Source Address Entropy (SAE)**:
   - Shannon entropy of source IP addresses
   - High values indicate greater randomization
   - Sudden increases suggest spoofing activity
   - Can be calculated over sliding time windows

4. **Flow Rule Match Ratio (FRMR)**:
   - Ratio of packets matching existing rules to total packets
   - Low values indicate potential table-miss flooding
   - Normal networks maintain relatively high ratios
   - Can be measured per switch or flow table

5. **Protocol Completion Ratio (PCR)**:
   - Ratio of completed protocol exchanges to initiated ones
   - Low values indicate potential attack traffic
   - Particularly useful for TCP-based attacks
   - Can be calculated per protocol type

#### 4.2 Composite Metrics

1. **Control Plane Pressure Index (CPPI)**:
   - Weighted combination of PIR, FCR, and controller CPU usage
   - Provides unified measure of control plane stress
   - Can incorporate adaptive weighting based on network conditions
   - Useful for triggering graduated response mechanisms

2. **Flow Anomaly Score (FAS)**:
   - Composite score based on multiple flow characteristics
   - Incorporates entropy measures, protocol behavior, and temporal patterns
   - Can be calculated using machine learning algorithms
   - Provides nuanced detection capability

3. **Distributed Attack Correlation Index (DACI)**:
   - Measures correlation of suspicious flows across multiple ingress points
   - Helps identify distributed attacks that might appear benign at individual points
   - Incorporates spatial and temporal correlation
   - Requires global network visibility

### 5. Target Flow Intensity Levels

#### 5.1 Low-Intensity Attacks

- **Characteristics**:
  - FCR: 10-50 new flows per second per switch
  - PIR: 5-25 packet-in messages per second per switch
  - SAE: Moderate to high (0.7-0.8 on normalized scale)
  - FRMR: 0.7-0.9 (70-90% match rate)
  - Duration: Often sustained over long periods (hours)

- **Impact**:
  - Minimal immediate performance degradation
  - Gradual resource consumption
  - Potential for evading detection
  - May serve as reconnaissance or testing phase

#### 5.2 Medium-Intensity Attacks

- **Characteristics**:
  - FCR: 50-200 new flows per second per switch
  - PIR: 25-100 packet-in messages per second per switch
  - SAE: High (0.8-0.9 on normalized scale)
  - FRMR: 0.5-0.7 (50-70% match rate)
  - Duration: Typically sustained for minutes to hours

- **Impact**:
  - Noticeable performance degradation
  - Significant resource consumption
  - Likely to trigger basic detection systems
  - May affect specific services or network segments

#### 5.3 High-Intensity Attacks

- **Characteristics**:
  - FCR: 200-1000+ new flows per second per switch
  - PIR: 100-500+ packet-in messages per second per switch
  - SAE: Very high (0.9+ on normalized scale)
  - FRMR: <0.5 (<50% match rate)
  - Duration: Often shorter periods (minutes) due to obvious nature

- **Impact**:
  - Severe performance degradation
  - Rapid resource exhaustion
  - Easily detectable but potentially devastating
  - May cause widespread service disruption

#### 5.4 Distributed Low-Rate Attacks

- **Characteristics**:
  - FCR: 5-20 new flows per second per switch, but across many switches
  - PIR: 2-10 packet-in messages per second per switch, aggregating at controller
  - SAE: High (0.8-0.9 on normalized scale)
  - FRMR: 0.7-0.9 (70-90% match rate)
  - DACI: High correlation across multiple ingress points
  - Duration: Typically sustained for hours

- **Impact**:
  - Difficult to detect at individual switch level
  - Cumulative impact at controller level
  - Bypasses local detection mechanisms
  - Requires global visibility for effective detection

### 6. Network-Specific Considerations

#### 6.1 Network Size and Topology

- **Small Networks (10-50 switches)**:
  - Lower baseline flow creation rates
  - More sensitive to flow anomalies
  - Tighter thresholds for detection
  - Faster propagation of attack effects

- **Medium Networks (50-200 switches)**:
  - Moderate baseline flow creation rates
  - Balanced detection sensitivity required
  - Potential for localized attack effects
  - Need for hierarchical detection approach

- **Large Networks (200+ switches)**:
  - Higher baseline flow creation rates
  - Risk of detection desensitization
  - Potential for targeted segment attacks
  - Essential to have distributed detection

#### 6.2 Traffic Patterns and Application Profiles

- **Web Service Networks**:
  - High legitimate HTTP/HTTPS flow rates
  - Need to distinguish from HTTP-based attacks
  - Focus on application-layer metrics
  - Protocol completion ratio particularly important

- **Data Center Networks**:
  - East-west traffic dominance
  - Higher baseline flow rates
  - Need for application-aware detection
  - Focus on traffic symmetry and protocol behavior

- **Campus/Enterprise Networks**:
  - Mixed traffic patterns
  - Periodic activity spikes (working hours)
  - Need for time-aware baseline adjustment
  - Balance between security and user experience

- **Service Provider Networks**:
  - Extremely high baseline traffic
  - Diverse application profiles
  - Need for customer-specific profiling
  - Focus on anomaly detection rather than absolute thresholds

### 7. Temporal Variations and Baseline Establishment

#### 7.1 Diurnal Patterns

- **Working Hours**:
  - Higher legitimate flow creation rates
  - Need for adjusted detection thresholds
  - Focus on anomaly detection rather than absolute values
  - Consider rate of change rather than absolute levels

- **Off-Hours**:
  - Lower legitimate flow creation rates
  - More sensitive detection thresholds
  - Potential for earlier attack detection
  - Higher suspicion for unusual activity

#### 7.2 Weekly Patterns

- **Weekday vs. Weekend**:
  - Different traffic profiles and baselines
  - Need for day-specific thresholds
  - Different application usage patterns
  - Adjusted normal entropy values

#### 7.3 Special Events

- **Planned Events (product launches, marketing campaigns)**:
  - Anticipated traffic spikes
  - Temporarily adjusted thresholds
  - Pre-emptive capacity allocation
  - Enhanced monitoring during events

- **Unplanned Events (breaking news, viral content)**:
  - Rapid traffic pattern changes
  - Need for adaptive threshold adjustment
  - Distinction from attack traffic
  - Correlation with external events

#### 7.4 Baseline Establishment Methods

- **Historical Analysis**:
  - Collection of traffic data over extended periods
  - Statistical analysis of normal variations
  - Establishment of confidence intervals
  - Seasonal adjustment factors

- **Machine Learning Approaches**:
  - Unsupervised learning for pattern recognition
  - Anomaly detection based on learned patterns
  - Continuous model updating
  - Adaptation to evolving network behavior

- **Hybrid Approaches**:
  - Combination of statistical and machine learning methods
  - Initial statistical baselines refined by machine learning
  - Periodic validation and adjustment
  - Human expert input for unusual situations
