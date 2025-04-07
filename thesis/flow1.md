# Flow Intensity Metrics and Thresholds for DDoS Detection in SDN

## 1. Core Flow Intensity Metrics

### 1.1 Volume-Based Metrics

#### 1.1.1 Packet-In Rate (PIR)
- **Definition**: Number of packet-in messages sent to the controller per second
- **Measurement Point**: Controller and/or individual switches
- **Calculation**: Count of packet-in messages over a defined time window (typically 1-5 seconds)
- **Significance**: Direct indicator of control plane load
- **Normal Range**: 
  - Small networks: 5-20 packet-in/sec
  - Medium networks: 20-100 packet-in/sec
  - Large networks: 100-500 packet-in/sec
- **Threshold Setting**:
  - Static threshold: Baseline + (2-3 × standard deviation)
  - Adaptive threshold: Moving average + dynamic multiplier based on network conditions

#### 1.1.2 Flow Creation Rate (FCR)
- **Definition**: Number of new flow rules installed per second
- **Measurement Point**: Controller and/or individual switches
- **Calculation**: Count of flow_mod messages over a defined time window
- **Significance**: Indicates rate of new traffic patterns requiring controller intervention
- **Normal Range**:
  - Small networks: 3-15 flows/sec
  - Medium networks: 15-75 flows/sec
  - Large networks: 75-300 flows/sec
- **Threshold Setting**:
  - Static threshold: Baseline + (2-3 × standard deviation)
  - Adaptive threshold: Moving average + dynamic multiplier based on time of day and network load

#### 1.1.3 Table-Miss Ratio (TMR)
- **Definition**: Ratio of table-miss packets to total packets processed
- **Measurement Point**: Individual switches
- **Calculation**: (Number of table-miss packets / Total packets) × 100%
- **Significance**: Indicates efficiency of flow rule installation and potential for control plane saturation
- **Normal Range**:
  - Initial network startup: 10-30%
  - Stable operation: 1-10%
  - Optimized networks: <1%
- **Threshold Setting**:
  - Static threshold: 2-3× baseline value
  - Adaptive threshold: Based on historical patterns and current network state

### 1.2 Distribution-Based Metrics

#### 1.2.1 Source IP Address Entropy (SIPE)
- **Definition**: Shannon entropy of source IP addresses in incoming packets
- **Measurement Point**: Individual switches or aggregation points
- **Calculation**: H(X) = -∑[P(xi) × log₂P(xi)] where P(xi) is the probability of source IP xi
- **Significance**: High entropy indicates greater randomization, potentially from spoofed addresses
- **Normal Range**:
  - Small networks: 0.3-0.6 (normalized)
  - Medium networks: 0.4-0.7 (normalized)
  - Large networks: 0.5-0.8 (normalized)
- **Threshold Setting**:
  - Static threshold: Baseline + 0.15-0.25
  - Adaptive threshold: Based on historical entropy patterns with time-of-day adjustments

#### 1.2.2 Destination IP Address Entropy (DIPE)
- **Definition**: Shannon entropy of destination IP addresses in incoming packets
- **Measurement Point**: Individual switches or aggregation points
- **Calculation**: H(X) = -∑[P(xi) × log₂P(xi)] where P(xi) is the probability of destination IP xi
- **Significance**: Sudden changes indicate shift in traffic distribution, potentially from attack
- **Normal Range**:
  - Small networks: 0.2-0.5 (normalized)
  - Medium networks: 0.3-0.6 (normalized)
  - Large networks: 0.4-0.7 (normalized)
- **Threshold Setting**:
  - Static threshold: Baseline + 0.15-0.25
  - Adaptive threshold: Based on historical entropy patterns with service-specific adjustments

#### 1.2.3 Port Number Entropy (PNE)
- **Definition**: Shannon entropy of source and destination port numbers
- **Measurement Point**: Individual switches or aggregation points
- **Calculation**: H(X) = -∑[P(xi) × log₂P(xi)] where P(xi) is the probability of port number xi
- **Significance**: High entropy in source ports often indicates randomized attack traffic
- **Normal Range**:
  - Source ports: 0.6-0.8 (normalized)
  - Destination ports: 0.3-0.6 (normalized)
- **Threshold Setting**:
  - Source ports: Baseline + 0.1-0.2
  - Destination ports: Baseline + 0.15-0.25

### 1.3 Temporal Metrics

#### 1.3.1 Flow Rule Lifetime (FRL)
- **Definition**: Average duration of installed flow rules before expiration or removal
- **Measurement Point**: Controller
- **Calculation**: Average time between flow rule installation and removal
- **Significance**: Short-lived flows may indicate attack traffic designed to consume resources
- **Normal Range**:
  - Interactive traffic: 30-120 seconds
  - Sustained connections: 120-600 seconds
  - Long-lived connections: >600 seconds
- **Threshold Setting**:
  - Alert on significant decrease in average lifetime
  - Threshold: <50% of baseline average

#### 1.3.2 Inter-Arrival Time Variance (IATV)
- **Definition**: Variance in time between consecutive packets of the same flow
- **Measurement Point**: Individual switches
- **Calculation**: Statistical variance of inter-packet arrival times
- **Significance**: Low variance may indicate automated attack traffic
- **Normal Range**: Highly variable based on application type
- **Threshold Setting**:
  - Application-specific thresholds
  - Alert on variance significantly below expected range

#### 1.3.3 Flow Establishment Rate Change (FERC)
- **Definition**: Rate of change in flow creation rate
- **Measurement Point**: Controller
- **Calculation**: First derivative of flow creation rate over time
- **Significance**: Sudden spikes indicate potential attack onset
- **Normal Range**:
  - Stable networks: ±10-20% change per minute
  - Dynamic networks: ±20-40% change per minute
- **Threshold Setting**:
  - Alert on changes exceeding 50% in short time windows (10-30 seconds)
  - Consider both absolute and percentage change

## 2. Composite Metrics

### 2.1 Control Plane Pressure Index (CPPI)
- **Definition**: Weighted combination of metrics indicating control plane stress
- **Components**:
  - Packet-In Rate (PIR)
  - Flow Creation Rate (FCR)
  - Controller CPU Utilization
  - Controller Memory Utilization
- **Calculation**:
  ```
  CPPI = w₁ × (PIR/PIR_threshold) + 
         w₂ × (FCR/FCR_threshold) + 
         w₃ × (CPU/CPU_threshold) + 
         w₄ × (MEM/MEM_threshold)
  ```
  where w₁ + w₂ + w₃ + w₄ = 1
- **Significance**: Unified measure of control plane health
- **Normal Range**: 0.3-0.7
- **Threshold Setting**:
  - Warning threshold: 0.7-0.8
  - Critical threshold: >0.8
  - Emergency threshold: >0.9

### 2.2 Flow Anomaly Score (FAS)
- **Definition**: Composite score based on multiple flow characteristics
- **Components**:
  - Source IP Entropy
  - Destination IP Entropy
  - Port Number Entropy
  - Protocol Distribution
  - Flow Rule Lifetime
- **Calculation**:
  ```
  FAS = w₁ × (SIPE/SIPE_threshold) + 
        w₂ × (DIPE/DIPE_threshold) + 
        w₃ × (PNE/PNE_threshold) + 
        w₄ × (PD_score) + 
        w₅ × (1 - FRL/FRL_baseline)
  ```
  where w₁ + w₂ + w₃ + w₄ + w₅ = 1
- **Significance**: Comprehensive measure of flow characteristics deviation
- **Normal Range**: 0.2-0.6
- **Threshold Setting**:
  - Warning threshold: 0.6-0.7
  - Alert threshold: >0.7
  - Critical threshold: >0.8

### 2.3 Distributed Attack Correlation Index (DACI)
- **Definition**: Measure of suspicious activity correlation across multiple switches
- **Components**:
  - Packet-In Rate correlation
  - Flow Creation Rate correlation
  - Entropy measure correlation
  - Spatial distribution of suspicious flows
- **Calculation**:
  ```
  DACI = w₁ × PIR_correlation + 
         w₂ × FCR_correlation + 
         w₃ × Entropy_correlation + 
         w₄ × Spatial_distribution_score
  ```
  where w₁ + w₂ + w₃ + w₄ = 1
- **Significance**: Identifies distributed attacks that might appear benign at individual points
- **Normal Range**: 0.1-0.4
- **Threshold Setting**:
  - Alert threshold: >0.5
  - Critical threshold: >0.7

## 3. Threshold Determination Methodologies

### 3.1 Static Threshold Approaches

#### 3.1.1 Statistical Analysis Based
- **Method**: Analyze historical data to establish baseline and standard deviation
- **Threshold Setting**: Baseline + (n × standard deviation), where n typically ranges from 2-3
- **Advantages**:
  - Simple to implement and understand
  - Computationally efficient
  - Stable detection boundaries
- **Disadvantages**:
  - Lacks adaptability to changing network conditions
  - Requires extensive historical data
  - May lead to high false positive/negative rates in dynamic environments
- **Recommended For**:
  - Stable networks with predictable traffic patterns
  - Metrics with low natural variation
  - Initial deployment before adaptive systems are calibrated

#### 3.1.2 Percentile-Based
- **Method**: Set thresholds based on percentiles of historical data distribution
- **Threshold Setting**: 95th-99th percentile of normal operation
- **Advantages**:
  - Robust against outliers
  - Does not assume normal distribution
  - Simple to implement
- **Disadvantages**:
  - Still lacks adaptability
  - Requires significant historical data
  - May be too conservative in some environments
- **Recommended For**:
  - Metrics with non-normal distributions
  - Networks with occasional legitimate traffic spikes
  - Complementary to other threshold methods

### 3.2 Adaptive Threshold Approaches

#### 3.2.1 Time-Series Analysis
- **Method**: Analyze temporal patterns to predict expected values and set dynamic thresholds
- **Techniques**:
  - Moving Average (MA)
  - Exponential Smoothing
  - Autoregressive Integrated Moving Average (ARIMA)
  - Seasonal Decomposition of Time Series (STL)
- **Advantages**:
  - Adapts to changing network conditions
  - Accounts for temporal patterns (time of day, day of week)
  - Reduces false positives during legitimate traffic variations
- **Disadvantages**:
  - More complex to implement
  - Computationally intensive
  - May adapt to slowly increasing attack traffic
- **Recommended For**:
  - Networks with strong temporal patterns
  - Metrics with predictable variations
  - Environments requiring high detection accuracy

#### 3.2.2 Machine Learning-Based
- **Method**: Use machine learning algorithms to dynamically adjust thresholds
- **Techniques**:
  - Supervised learning (requires labeled data)
  - Unsupervised learning (anomaly detection)
  - Reinforcement learning (adaptive policy optimization)
- **Advantages**:
  - Highly adaptive to complex patterns
  - Can incorporate multiple features simultaneously
  - Potential for very high detection accuracy
- **Disadvantages**:
  - Requires significant computational resources
  - May need extensive training data
  - "Black box" nature can make troubleshooting difficult
- **Recommended For**:
  - Complex networks with unpredictable patterns
  - Environments requiring highest detection accuracy
  - Scenarios where multiple metrics must be considered together

### 3.3 Hybrid Approaches

#### 3.3.1 Multi-Level Thresholds
- **Method**: Implement multiple threshold levels for graduated response
- **Implementation**:
  - Warning threshold: Static or loosely adaptive
  - Alert threshold: Moderately adaptive
  - Critical threshold: Highly adaptive or ML-based
- **Advantages**:
  - Balances stability with adaptability
  - Provides graduated response options
  - Combines strengths of different approaches
- **Disadvantages**:
  - More complex to implement and manage
  - Requires tuning multiple thresholds
  - Potential for conflicting indicators
- **Recommended For**:
  - Production environments requiring high reliability
  - Critical infrastructure protection
  - Scenarios with graduated response mechanisms

#### 3.3.2 Context-Aware Thresholds
- **Method**: Adjust thresholds based on network context and state
- **Contextual Factors**:
  - Current network load
  - Active services and applications
  - Recent security events
  - External factors (e.g., marketing campaigns)
- **Advantages**:
  - Highly relevant to current network state
  - Reduces false positives during legitimate events
  - Can incorporate human intelligence
- **Disadvantages**:
  - Requires extensive context monitoring
  - Complex decision logic
  - Potential for manual override abuse
- **Recommended For**:
  - Networks with highly variable legitimate traffic
  - Environments with scheduled events affecting traffic
  - Systems with human security analysts in the loop

## 4. Threshold Calibration Process

### 4.1 Initial Threshold Establishment

#### 4.1.1 Baseline Data Collection
- **Duration**: Minimum 2 weeks, ideally 4-8 weeks
- **Coverage**: Must include:
  - Weekday and weekend patterns
  - Business hours and off-hours
  - Month-end processing (if applicable)
  - Any regular network events
- **Metrics**: Collect all relevant metrics at appropriate intervals
- **Storage**: Retain raw data for future recalibration

#### 4.1.2 Statistical Analysis
- **Basic Statistics**:
  - Mean, median, mode
  - Standard deviation
  - Percentiles (50th, 75th, 90th, 95th, 99th)
  - Min/max values
- **Pattern Analysis**:
  - Diurnal patterns
  - Weekly patterns
  - Monthly patterns (if applicable)
  - Correlation between metrics

#### 4.1.3 Initial Threshold Setting
- **Conservative Approach**:
  - Set thresholds high initially to minimize false positives
  - Volume metrics: 99th percentile or (mean + 3σ)
  - Distribution metrics: 95th percentile or (mean + 2σ)
  - Composite metrics: 95th percentile
- **Document Baseline**:
  - Record all initial thresholds
  - Document rationale for each threshold
  - Establish review schedule

### 4.2 Threshold Tuning

#### 4.2.1 Controlled Testing
- **Simulated Attacks**:
  - Low-volume attacks
  - Medium-volume attacks
  - High-volume attacks
  - Distributed low-rate attacks
- **Metrics Monitoring**:
  - Record all metric values during tests
  - Identify detection gaps
  - Measure detection time
  - Evaluate false positive/negative rates

#### 4.2.2 Iterative Adjustment
- **Threshold Refinement**:
  - Adjust thresholds based on test results
  - Balance detection sensitivity with false positive rate
  - Consider operational impact of false positives
  - Document all adjustments and rationales
- **Validation Testing**:
  - Repeat testing with adjusted thresholds
  - Verify improved detection performance
  - Ensure no regression in other areas

#### 4.2.3 Production Monitoring
- **Initial Deployment**:
  - Deploy in monitoring-only mode initially
  - Record all threshold triggers without automated response
  - Manually validate each trigger
  - Document false positives and missed detections
- **Gradual Activation**:
  - Enable automated responses for high-confidence detections first
  - Gradually expand to medium-confidence detections
  - Maintain human verification for low-confidence detections

### 4.3 Continuous Improvement

#### 4.3.1 Regular Review
- **Schedule**:
  - Weekly review during initial deployment
  - Monthly review during normal operation
  - Immediate review after any confirmed attack
- **Analysis**:
  - Review all threshold triggers
  - Analyze false positives and false negatives
  - Evaluate detection timing
  - Consider threshold adjustments

#### 4.3.2 Adaptive Learning
- **Machine Learning Integration**:
  - Train models on collected data
  - Implement supervised learning with labeled events
  - Consider unsupervised anomaly detection
  - Gradually increase reliance on ML-based thresholds
- **Feedback Loop**:
  - Incorporate analyst feedback
  - Learn from confirmed attacks
  - Adjust to changing network conditions
  - Document model performance improvements

## 5. Network-Specific Threshold Considerations

### 5.1 Network Size Adjustments

#### 5.1.1 Small Networks (10-50 switches)
- **Packet-In Rate**: Lower baseline, tighter thresholds
  - Warning: 2× baseline
  - Critical: 3× baseline
- **Flow Creation Rate**: More sensitive to changes
  - Warning: 1.5× baseline
  - Critical: 2.5× baseline
- **Entropy Measures**: Typically lower baseline entropy
  - Warning: Baseline + 0.15
  - Critical: Baseline + 0.25

#### 5.1.2 Medium Networks (50-200 switches)
- **Packet-In Rate**: Moderate baseline, balanced thresholds
  - Warning: 1.75× baseline
  - Critical: 2.5× baseline
- **Flow Creation Rate**: Moderate sensitivity
  - Warning: 1.7× baseline
  - Critical: 2.3× baseline
- **Entropy Measures**: Moderate baseline entropy
  - Warning: Baseline + 0.12
  - Critical: Baseline + 0.2

#### 5.1.3 Large Networks (200+ switches)
- **Packet-In Rate**: Higher baseline, wider thresholds
  - Warning: 1.5× baseline
  - Critical: 2× baseline
- **Flow Creation Rate**: Lower sensitivity to changes
  - Warning: 1.5× baseline
  - Critical: 2× baseline
- **Entropy Measures**: Higher baseline entropy
  - Warning: Baseline + 0.1
  - Critical: Baseline + 0.15

### 5.2 Network Type Adjustments

#### 5.2.1 Data Center Networks
- **Key Metrics**:
  - East-west traffic ratio
  - VM migration events
  - Application-specific flow patterns
- **Threshold Adjustments**:
  - Higher tolerance for flow creation spikes
  - Application-aware thresholds
  - Service-specific entropy baselines

#### 5.2.2 Campus/Enterprise Networks
- **Key Metrics**:
  - User authentication events
  - North-south traffic ratio
  - Time-of-day patterns
- **Threshold Adjustments**:
  - Time-aware thresholds (working hours vs. off-hours)
  - User density-based adjustments
  - Service access pattern monitoring

#### 5.2.3 Service Provider Networks
- **Key Metrics**:
  - Customer traffic isolation
  - Peering point monitoring
  - Service-specific traffic patterns
- **Threshold Adjustments**:
  - Customer-specific baselines
  - Higher overall thresholds
  - Service-specific detection criteria

### 5.3 Application Profile Adjustments

#### 5.3.1 Web Service Environments
- **Key Metrics**:
  - HTTP/HTTPS request patterns
  - Session establishment rate
  - Content delivery patterns
- **Threshold Adjustments**:
  - Higher tolerance for source IP entropy
  - Content popularity-aware thresholds
  - Session behavior monitoring

#### 5.3.2 Database/Transaction Environments
- **Key Metrics**:
  - Transaction rate
  - Query complexity
  - Connection persistence
- **Threshold Adjustments**:
  - Lower tolerance for connection pattern changes
  - Transaction rate-aware thresholds
  - Stricter protocol conformance checking

#### 5.3.3 Mixed Application Environments
- **Key Metrics**:
  - Application mix ratio
  - Service interdependency
  - Resource utilization balance
- **Threshold Adjustments**:
  - Service-specific thresholds
  - Correlation-based detection
  - Application dependency-aware monitoring

## 6. Implementation Considerations

### 6.1 Measurement Frequency

#### 6.1.1 Real-time Metrics
- **Metrics**:
  - Packet-In Rate
  - Flow Creation Rate
  - Table-Miss Ratio
- **Sampling Interval**: 1-5 seconds
- **Aggregation Window**: 10-30 seconds
- **Storage Considerations**: Circular buffer with summary statistics

#### 6.1.2 Near-real-time Metrics
- **Metrics**:
  - Entropy Measures
  - Flow Rule Lifetime
  - Composite Metrics
- **Sampling Interval**: 10-30 seconds
  - **Aggregation Window**: 1-5 minutes
  - **Storage Considerations**: Time-series database with downsampling

#### 6.1.3 Trend Analysis Metrics
- **Metrics**:
  - Baseline Deviations
  - Long-term Pattern Changes
  - Correlation Indices
- **Sampling Interval**: 5-15 minutes
- **Aggregation Window**: 1 hour to 1 day
- **Storage Considerations**: Time-series database with retention policies

### 6.2 Computational Efficiency

#### 6.2.1 Distributed Calculation
- **Switch-Level Calculations**:
  - Basic packet and flow counting
  - Simple ratio calculations
  - Initial filtering of obvious attacks
- **Aggregation-Level Calculations**:
  - Entropy measures
  - Flow pattern analysis
  - Regional correlation
- **Controller-Level Calculations**:
  - Global correlation analysis
  - Complex composite metrics
  - Machine learning models

#### 6.2.2 Optimization Techniques
- **Sampling**:
  - Packet sampling for high-volume links
  - Flow sampling for large networks
  - Adaptive sampling rate based on load
- **Incremental Calculation**:
  - Running statistics (mean, variance)
  - Sliding window entropy calculation
  - Incremental model updates
- **Parallel Processing**:
  - Metric calculation parallelization
  - Distributed detection agents
  - Workload distribution across controllers

### 6.3 Storage Requirements

#### 6.3.1 Short-term Storage
- **Purpose**: Real-time detection and immediate analysis
- **Data Retention**: 1-7 days
- **Resolution**: Full resolution (original sampling rate)
- **Storage Type**: In-memory database or high-performance time-series database

#### 6.3.2 Medium-term Storage
- **Purpose**: Pattern analysis and threshold tuning
- **Data Retention**: 30-90 days
- **Resolution**: Medium resolution (5-15 minute aggregates)
- **Storage Type**: Time-series database with compression

#### 6.3.3 Long-term Storage
- **Purpose**: Baseline establishment and trend analysis
- **Data Retention**: 1-2 years
- **Resolution**: Low resolution (hourly or daily aggregates)
- **Storage Type**: Compressed time-series database or data warehouse

### 6.4 Integration with Mobile Agent Architecture

#### 6.4.1 Agent Monitoring Responsibilities
- **Switch-Level Agents**:
  - Local metric collection
  - Preliminary threshold monitoring
  - Initial attack detection
  - Local traffic filtering
- **Controller-Level Agent**:
  - Global metric aggregation
  - Complex metric calculation
  - Correlation analysis
  - Threshold adjustment
- **Clone Agents**:
  - Target-specific monitoring
  - Local attack verification
  - Direct mitigation actions
  - Feedback to controller agent

#### 6.4.2 Threshold Distribution
- **Centralized Definition**:
  - Base thresholds defined at controller
  - Global network view for context
  - Consistent policy enforcement
- **Local Adaptation**:
  - Switch agents adjust to local conditions
  - Context-specific threshold modifications
  - Temporary adjustments during attacks
- **Synchronization**:
  - Regular threshold updates from controller
  - Local adaptation reporting
  - Conflict resolution mechanisms

#### 6.4.3 Detection Coordination
- **Hierarchical Detection**:
  - Local detection at switch level
  - Regional correlation at aggregation level
  - Global analysis at controller level
- **Collaborative Detection**:
  - Information sharing between agents
  - Coordinated threshold adjustments
  - Distributed attack recognition
- **Escalation Procedures**:
  - Graduated response based on confidence
  - Multi-level verification
  - Coordinated mitigation actions
